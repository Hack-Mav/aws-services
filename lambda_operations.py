from aws_clients import lambda_client
from botocore.exceptions import ClientError

def invoke_lambda_function(function_name, payload):
    try:
        response = lambda_client.invoke(
            FunctionName=function_name,
            InvocationType='RequestResponse',
            Payload=payload
        )
        print("Lambda function invoked successfully.")
        print("Response:", response['Payload'].read().decode('utf-8'))
    except ClientError as e:
        print(f"Error invoking Lambda function: {e}")
