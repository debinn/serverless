import boto3

def lambda_handler(event, context):
    client = boto3.client('dynamodb')
    response = client.create_backup(
        TableName='video',
        BackupName='Video-backup'
    )
    return "success"

