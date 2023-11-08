import aws_cdk.aws_ec2 as ec2
import aws_cdk as cdk
import aws_cdk.aws_opensearchservice as es
import aws_cdk.aws_cognito as cognito
# basic VPC configs


REGION = 'us-east-2'
ACCOUNT = '080266302756'




route53_conf = {
    "hostedzone_id": "Z05045244G4M5OFGHB4C",
    "record_name": "reactapp.abdelalitraining.com",
    "certificate_arn": "arn:aws:acm:us-east-1:080266302756:certificate/326d29bd-95af-4139-ace0-eccb94dbbcfe"
}
