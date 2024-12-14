from aws_clients import ec2
from botocore.exceptions import ClientError

def launch_ec2_instance():
    try:
        response = ec2.run_instances(
            ImageId='ami-0614680123427b75e',
            InstanceType='t2.micro',
            MinCount=1,
            MaxCount=1,
            KeyName='my-key-pair',
        )
        print("EC2 Instance launched successfully:", response['Instances'][0]['InstanceId'])
    except ClientError as e:
        print(f"Error launching EC2 instance: {e}")

def describe_ec2_instances():
    try:
        response = ec2.describe_instances()
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                print(f"Instance ID: {instance['InstanceId']}, State: {instance['State']['Name']}")
    except ClientError as e:
        print(f"Error describing EC2 instances: {e}")
