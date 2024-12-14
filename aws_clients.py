import boto3

# AWS service clients
s3 = boto3.client('s3')
ec2 = boto3.client('ec2')
lambda_client = boto3.client('lambda')
dynamodb = boto3.client('dynamodb')
