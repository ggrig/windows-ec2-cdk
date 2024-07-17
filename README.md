
# Windows EC2 with ready to connect RDP in AWS CDK

## Description
This is a simple project showing how to create a Windows EC2 machine, with ready to connect RDP. Project is a complete solution which after deployment provides for us preconfigured .rdp file to connect to our EC2. It also extracts Admin password from EC2 so it can be used to login to the machine. Main goal for this project was a possibility to not use AWS console in any phase and deploy everything from the code.

## Prerequisite
 * AWS CDK CLI
 * AWS CLI
 * node.js
 * Python 3.12
 * Poetry (installed [manually](https://python-poetry.org/docs/#installing-manually))
 * RDP client

## Quick start
1. Clone the repo
   ```sh
   git clone git@github.com:amswiatkowski/windows-ec2-cdk.git
   ```
2. Install dependencies
    ```sh
    poetry install
    ```
3. Deploy the project
   ```sh
   ./deploy.sh
   ```
4. Open created `client_ec2_connection.rdp` file and connect to the EC2. Use the password from the console's output.


## Useful commands
 * `./lint.sh`          Fixes indents and checks your code quality
 * `./destroy.sh --region us-east-1`       Triggers cdk destroy
 * `./deploy/sh --region us-east-1`        Deploys stack to the AWS account
 * `pytest -vv ./tests` Run tests

## Useful links
* [AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/cli.html)
* [Microsoft Remote Desktop](https://apps.microsoft.com/detail/9wzdncrfj3ps?hl=en-US&gl=US)

## Author
**Adam Świątkowski**
* [github/amswiatkowski](https://github.com/amswiatkowski)
* [Blog](https://cloudybarz.com/)

### License
Copyright © 2024, [Adam Świątkowski](https://github.com/amswiatkowski).
Released under the [MIT License](LICENSE).

