# pylint: disable=unused-variable
from aws_cdk import Stack
from constructs import Construct
from windows_ec2.windows_ec2_construct import KnimeVMConstruct


class KnimeVMStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        windows_ec2_construct = KnimeVMConstruct(self,
                                                    "KnimeVMConstruct")
