from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
)
from aws_cdk import RemovalPolicy, CfnOutput
from constructs import Construct
import aws_cdk.aws_cloudfront as cloudfront
import aws_cdk.aws_cloudfront_origins as origins
import aws_cdk.aws_certificatemanager as certificate
import  aws_cdk.aws_s3 as s3
import aws_cdk.aws_route53 as route53

from config import (
    route53_conf
    
    )

class CdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        bucket_name = self.node.try_get_context('bucket_name')
        
        s3_bucket = s3.Bucket(
            self, "MyBucket",
            bucket_name= bucket_name,
            removal_policy= RemovalPolicy.DESTROY
        )
        
        distribution = cloudfront.Distribution(self, "AwsCloudfrontDistribution",
                default_behavior=cloudfront.BehaviorOptions(
                    allowed_methods=cloudfront.AllowedMethods.ALLOW_ALL,
                    viewer_protocol_policy=cloudfront.ViewerProtocolPolicy.REDIRECT_TO_HTTPS,
                    origin=origins.S3Origin(s3_bucket)
                ),
                error_responses= [
                    cloudfront.ErrorResponse(
                          http_status=403,
                          response_http_status=200,
                          response_page_path="/index.html"
                        )
                    ],
                certificate=certificate.Certificate.from_certificate_arn(self, 
                    "AWSCertificateManager",
                    route53_conf['certificate_arn']
                    ),
                domain_names=[route53_conf['record_name']],
                
        )
        
        CfnOutput(self, "distributionid", value=distribution.distribution_id)
        # Route53
        route53.CfnRecordSetGroup(self,"AWSCloudFrontRecord",
           hosted_zone_id=route53_conf['hostedzone_id'],
           comment="cloudfront route53 record",
           record_sets=[
               route53.CfnRecordSetGroup.RecordSetProperty(
                    name=route53_conf['record_name'],
                    type='A',
                    alias_target=route53.CfnRecordSetGroup.AliasTargetProperty(
                      dns_name=distribution.domain_name,
                      hosted_zone_id="Z2FDTNDATAQYW2"
                    )
               )
               ]
        )