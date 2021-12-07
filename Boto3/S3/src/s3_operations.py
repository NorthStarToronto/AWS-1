import boto3
import yaml

with open("src/conf/config.yml", "r") as yamlfile:
    cfg = yaml.load(yamlfile, Loader=yaml.FullLoader)

# Enable pyboto3 auto completion function
def s3_client():
    s3 = boto3.client('s3')
    """ :type : pyboto3.s3 """
    return s3

# Create a s3 bucket
def create_bucket(bucket_name):
    return s3_client().create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
            'LocationConstraint': 'us-east-2'
        }
    )

# Create a bucket policy
def create_bucket_policy():
    bucket_policy={
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "statement1",
                "Effect": "Allow",
                "Principal": "*",
                "Action": [
                    "s3:PutObject",
                    "s3:PubObjectAcl"
                ],
                "Resource": "arn:aws:s3:::jason-lee-us-east-1-boto3-test-bucket/*"
            },
            {
                "Sid": "statement2",
                "Effect": "Allow",
                "Principal": "*",
                "Action": [
                    "s3:CreateBucket",
                    "s3:ListAllMyBuckets",
                    "s3:GetBucketLocation"
                ],
                "Resource": "arn:aws:s3:::*"
            }
        ]
    }

    # Overwrite the existing bucket policy
    policy_string = json.dumps(bucket_policy)
    return s3_client.put_bucket_policy()

# listing buckets
def list_buckets():
    return s3_client.list_buckets()

# getting bucket properties
def get_bucket_policy(bucket_name):
    return s3_client.get_bucket_policy(bucket_name)
    
# getting bucket encryption
def get_bucket_encryption(bucket_name):
    return s3_client.get_bucket_encryption(bucket_name)

# updating bucket policy
def update_bucket_policy(bucket_name):
    bucket_policy={
        'Version: '2012-10-17',
        'Statement': [
            {
                'Sid': 'statement3',
                'Effect': 'Allow',
                'Principal': '*',
                'Action': [
                    's3:DeleteObject',
                    's3:GetObject',
                    's3:PutObject'
                ],
                'Resource': 'arn:aws:s3:::' + bucket_name + '/*'

            }
        ]
    }

    policy_string = json.dumps(bucket_policy)
    # Overwrite the existing bucket policy
    return s3_client.put_bucket_policy(
        Bucket=bucket_name,
        Policy=policy_string
    )

def server_side_encrypt_bucket(bucket_name):
    return s3_client.server_side_encrypt_bucket(
        Bucket=bucket_name,
        ServerSideEncryptionConfiguration={
            'Rules': [
                {
                    'ApplyServerSideEncryptionByDefault': {
                        'Algorithm': 'AES256'
                    }
                }
            ]
        }
    )


# deleting buckets
def delete_bucket(bucket_name):
    return s3_client.delete_bucket(bucket_name)

if __name__ == '__main__' :
    # Print the response from the S3 create bucket api
    print(create_bucket(cfg["bucket"]["test"]))
    print(create_bucket_policy)
    print(list_buckets())
    print(get_bucket_policy(cfg["bucket"]["test"]))
    print(get_bucket_encryption(cfg["bucket"]["test"]))
    print(update_bucket_policy(cfg["bucket"]["test"]))
    print(server_side_encrypt_bucket(cfg["bucket"]["test"]))


    