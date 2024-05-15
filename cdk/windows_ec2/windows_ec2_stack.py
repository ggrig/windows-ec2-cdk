# pylint: disable=unused-variable
from aws_cdk import Stack
from constructs import Construct
from windows_ec2.hosted_zone_route53.route_53_hosted_zone_construct import \
    Route53HostedZoneConstruct
from windows_ec2.hosted_zone_route53.route_53_hosted_zone_records_construct import \
    Route53HostedZoneRecordsConstruct
from windows_ec2.webserver_ec2.ec2_web_server_construct import \
    Ec2WebserverConstruct


class WindowsEC2Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        windows_ec2_construct = WindowsEC2Construct(
            self, "WindowsEC2Construct")
