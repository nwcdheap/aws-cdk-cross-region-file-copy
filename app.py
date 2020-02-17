#!/usr/bin/env python3

from aws_cdk import core

from crrcopy.crrcopy_stack import MyStack


app = core.App()
MyStack(app, "crrcopy-cdk", env={'account': '','region': ''})
app.synth()
