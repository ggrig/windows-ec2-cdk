#!/usr/bin/env python3
# pylint: disable=broad-exception-caught
import os
from pathlib import Path
from typing import Final

from aws_cdk import App, Environment
from boto3 import client, session
from git import Repo
from windows_ec2.constants import SERVICE_NAME
from windows_ec2.windows_ec2_stack import \
    LatencyBasedRoutingStack


def get_username() -> str:
    DEFAULT_USERNAME: Final[str] = 'github'
    try:
        login = os.getlogin().replace('.', '')
        if login == 'root':
            login = os.getenv("USER")
        if login is None:
            return DEFAULT_USERNAME
        return login
    except Exception:
        return DEFAULT_USERNAME


def get_stack_name() -> str:
    repo = Repo(Path.cwd())
    username = get_username()
    try:
        return f'{username}{SERVICE_NAME}{repo.active_branch}'
    except TypeError:
        return f'{username}{SERVICE_NAME}'


account = client('sts').get_caller_identity()['Account']
region = session.Session().region_name
app = App()
windows_ec2_stack = WindowsEC2Stack(
    app,
    get_stack_name(),
    description='Complete Windows EC2 Stack',
    env=Environment(account=os.environ.get('AWS_DEFAULT_ACCOUNT', account),
                    region=os.environ.get('AWS_DEFAULT_REGION', region)),
)
app.synth()
