import os

from windows_ec2.constants import MASTER_REGION


def is_master_region() -> bool:
    return os.getenv('REGION').lower() == MASTER_REGION
