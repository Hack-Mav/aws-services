from aws_clients import dynamodb
from botocore.exceptions import ClientError

def create_dynamodb_table(table_name):
    try:
        response = dynamodb.create_table(
            TableName=table_name,
            KeySchema=[
                {'AttributeName': 'id', 'KeyType': 'HASH'}
            ],
            AttributeDefinitions=[
                {'AttributeName': 'id', 'AttributeType': 'S'}
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )
        print(f"DynamoDB table '{table_name}' created successfully.")
    except ClientError as e:
        print(f"Error creating DynamoDB table: {e}")

def put_item_dynamodb(table_name, item):
    try:
        dynamodb.put_item(TableName=table_name, Item=item)
        print(f"Item inserted successfully into {table_name}.")
    except ClientError as e:
        print(f"Error inserting item into DynamoDB: {e}")

def get_item_dynamodb(table_name, key):
    try:
        response = dynamodb.get_item(TableName=table_name, Key=key)
        if 'Item' in response:
            print(f"Item retrieved: {response['Item']}")
        else:
            print(f"Item not found in {table_name}.")
    except ClientError as e:
        print(f"Error retrieving item from DynamoDB: {e}")
