import boto3


def connect_to_s3(
    endpoint_url: str, access_key_id: str, secret_access_key: str
) -> boto3.client:
    try:
        s3_client = boto3.client(
            "s3",
            endpoint_url=endpoint_url,
            aws_access_key_id=access_key_id,
            aws_secret_access_key=secret_access_key,
        )
        print("Succesfully connected to S3")
        return s3_client
    except Exception as e:
        print(f"Error while connecting to S3: {e}")