#!/bin/bash

echo "This script will delete CloudFormation stacks created."
echo "Please confirm by entering the stack name(s) you want to deactivate."

# Read input from user
read -p "Stack Name: " StackName

# Delete the specified stack
aws cloudformation delete-stack --stack-name "$StackName"
