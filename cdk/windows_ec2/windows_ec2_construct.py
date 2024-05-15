from typing import Final

from aws_cdk import CfnOutput
from constructs import Construct


class WindowsEC2Construct(Construct):
    _RDP_PORT: Final[int] = 3389
    # pylint: disable=consider-using-with
    def __init__(self, scope: Construct, stack_id: str) -> None:
        super().__init__(scope, stack_id)
        self.vpc = ec2.Vpc(
            self,
            "ClientVPC",
            max_azs=1,
            subnet_configuration=[ec2.SubnetConfiguration(
                name="public-subnet-1",
                subnet_type=ec2.SubnetType.PUBLIC,
                cidr_mask=24,
            )],
        )
        self.ec2_sg = ec2.SecurityGroup(self, "ClientSecurityGroup", vpc=self.vpc, allow_all_outbound=True)
        
        self.role = iam.Role(self, 'ClientRole', assumed_by=iam.ServicePrincipal('ec2.amazonaws.com'))
        self.role.add_managed_policy(iam.ManagedPolicy.from_aws_managed_policy_name('AmazonSSMManagedInstanceCore'))

        self.instance = ec2.Instance(
            self, "ClientEC2", instance_name='ClientEC2', instance_type=ec2.InstanceType.of(ec2.InstanceClass.T3, ec2.InstanceSize.MEDIUM),
            machine_image=ec2.MachineImage.latest_windows(version=ec2.WindowsVersion.WINDOWS_SERVER_2022_ENGLISH_FULL_BASE), vpc=self.vpc,
            security_group=self.ec2_sg, role=self.role, associate_public_ip_address=True, key_name=EC2_KEY_NAME)
        CfnOutput(self, id='ClientEC2_ID', value=self.instance.instance_id).override_logical_id('EC2ID')
        CfnOutput(self, id='ClientEC2_IP', value=self.instance.instance_public_ip).override_logical_id('EC2IP')
        CfnOutput(self, id='ClientEC2_PORT', value=str(self._RDP_PORT)).override_logical_id('EC2PORT')
        CfnOutput(self, id='ClientEC2_USERNAME', value='Administrator').override_logical_id('EC2USERNAME')

    def _generate_key_pair(self) -> None:
        ec2_client: EC2Client = boto3.client('ec2', region_name=self.region)
        ec2_client.delete_key_pair(KeyName=EC2_KEY_NAME)
        keypair = ec2_client.create_key_pair(KeyName=EC2_KEY_NAME)
        with open('client_ec2_key.pem', 'w', encoding='utf-8') as f:
            f.write(keypair.get('KeyMaterial'))
