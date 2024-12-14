import boto3
from botocore.exceptions import NoCredentialsError

# Create an S3 client
s3 = boto3.client('s3')

# Upload a file to S3
def upload_file(file_name, bucket_name):
    try:
        s3.upload_file(file_name, bucket_name, file_name)
        print(f"File '{file_name}' uploaded successfully to {bucket_name}.")
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except NoCredentialsError:
        print("Credentials not available.")
    except Exception as e:
        print(f"Error uploading file: {e}")

# List files in an S3 bucket
def list_files(bucket_name):
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

# Download a file from S3
def download_file(file_name, bucket_name, download_path):
    try:
        s3.download_file(bucket_name, file_name, download_path)
        print(f"File '{file_name}' downloaded successfully from {bucket_name} to {download_path}.")
    except FileNotFoundError:
        print(f"File '{file_name}' not found in the local directory.")
    except NoCredentialsError:
        print("Credentials not available.")
    except Exception as e:
        print(f"Error downloading file: {e}")

# Example Usage
if __name__ == "__main__":
    # Replace with your actual bucket name
    bucket_name = 'test-bucket-by-parthiv'
    file_name = 'titanic.csv'  # Replace with the file you want to upload

    # Upload a file to the S3 bucket
    upload_file(file_name, bucket_name)

    # List all files in the S3 bucket
    list_files(bucket_name)

    # Download a file from the S3 bucket
    download_file(file_name, bucket_name, f"downloaded_{file_name}")
