#!/bin/bash
while test $# -gt 0; do
    case "$1" in
    --region)
        shift
        export REGION=$1
        shift
        ;;
    --deploy_env)
        shift
        export DEPLOY_ENV=$2
        shift
        ;;
    *)
        echo "$1 is not a recognized flag!"
        return 1
        ;;
    esac
done
if [ -z "$REGION" ]; then
    REGION="eu-central-1"
fi
if [ -z "$DEPLOY_ENV" ]; then
    DEPLOY_ENV="dev"
fi
echo "Region: $REGION"
echo "Environment: $DEPLOY_ENV"
# Clean old keys if they do exist
./utils/clean_old_key_pairs_for_ec2.py
AWS_REGION=$REGION AWS_DEFAULT_REGION=$REGION DEPLOY_ENV=$DEPLOY_ENV cdk destroy --all --force --verbose
REGION=$REGION AWS_REGION=$REGION AWS_DEFAULT_REGION=$REGION DEPLOY_ENV=$DEPLOY_ENV cdk deploy --all --verbose --region $REGION --require-approval never
if [ $? -eq 0 ]; then
    echo "cdk deploy command was successful."
    # Wait for 5 minutes for the instance to be up and running
    echo "Waiting for the instance to be up and running..."
    sleep 300
    # Execute the generate_rdp_file.py script
    ./utils/generate_rdp_file.py
else
    echo "cdk deploy command failed."
    exit 1
fi