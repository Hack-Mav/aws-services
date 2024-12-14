from aws_clients import s3
from botocore.exceptions import NoCredentialsError

def upload_file_s3(file_name, bucket_name):
    try:
        s3.upload_file(file_name, bucket_name, file_name)
        print(f"File '{file_name}' uploaded successfully to {bucket_name}.")
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except NoCredentialsError:
        print("Credentials not available.")
    except Exception as e:
        print(f"Error uploading file: {e}")

def list_files_s3(bucket_name):
    try:
        response = s3.list_objects_v2(Bucket=bucket_name)
        if 'Contents' in response:
            print(f"Files in '{bucket_name}':")
            for item in response['Contents']:
                print(item['Key'])
        else:
            print(f"No files found in '{bucket_name}'.")
    except NoCredentialsError:
        print("Credentials not available.")
    except Exception as e:
        print(f"Error listing files: {e}")
