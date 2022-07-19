#!/usr/bin/env python3

import aws_cdk as cdk

from project_blue.project_blue_stack import ProjectBlueStack

app = cdk.App()
ProjectBlueStack(app, "project-blue")

app.synth()
