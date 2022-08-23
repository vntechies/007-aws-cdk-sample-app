#!/usr/bin/env python3

import aws_cdk as cdk

from aws_cdk_sample_app.aws_cdk_sample_app_stack import AwsCdkSampleAppStack


app = cdk.App()
AwsCdkSampleAppStack(app, "aws-cdk-sample-app")

app.synth()
