from s3_operations import upload_file_s3, list_files_s3
from ec2_operations import launch_ec2_instance, describe_ec2_instances
from lambda_operations import invoke_lambda_function
from dynamodb_operations import create_dynamodb_table, put_item_dynamodb, get_item_dynamodb

if __name__ == "__main__":
    # S3 Operations
    bucket_name = 'test-bucket-by-parthiv'
    file_name = 'titanic.csv'
    upload_file_s3(file_name, bucket_name)
    list_files_s3(bucket_name)

    # EC2 Operations
    launch_ec2_instance()
    describe_ec2_instances()

    # Lambda Operations
    function_name = 'my-first-lambda-function'
    payload = '{"key": "value"}'
    invoke_lambda_function(function_name, payload)

    # DynamoDB Operations
    table_name = 'my-first-table'
    create_dynamodb_table(table_name)
    item = {'id': {'S': '123'}, 'name': {'S': 'John Doe'}, 'age': {'N': '30'}}
    put_item_dynamodb(table_name, item)
    key = {'id': {'S': '123'}}
    get_item_dynamodb(table_name, key)
