from typing import Final

from aws_cdk import CfnOutput
from constructs import Construct


class WindowsEC2Construct(Construct):
    _RDP_PORT: Final[int] = 3389
    # pylint: disable=consider-using-with
    def __init__(self, scope: Construct, stack_id: str) -> None:
        super().__init__(scope, stack_id)



        CfnOutput(self,
                  "WebserverLoadBalancer",
                  export_name="WebserverLoadBalancer",
                  value=self.lb.load_balancer_dns_name)
