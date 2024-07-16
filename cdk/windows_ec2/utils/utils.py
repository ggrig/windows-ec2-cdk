# pylint: disable=broad-exception-caught
import os
from pathlib import Path
from typing import Final

from git import Repo
from windows_ec2.constants import SERVICE_NAME


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
        return f'{username}{SERVICE_NAME}'
    except TypeError:
        return f'{SERVICE_NAME}'