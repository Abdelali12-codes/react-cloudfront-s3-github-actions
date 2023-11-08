#!/usr/bin/env python3
import os

import aws_cdk as cdk

from cdk_stack import CdkStack
import config



cdk_env = cdk.Environment(region=config.REGION, account=config.ACCOUNT)


app = cdk.App()

CdkStack(app, "cloudfront-s3",env=cdk_env)

app.synth()
