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
    "certificate_arn": "arn:aws:acm:us-west-2:080266302756:certificate/7048596d-aa16-49f5-8399-2b2e53a4fc5f"
}
