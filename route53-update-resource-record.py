import boto3

client = boto3.client('route53')
response = client.change_resource_record_sets(
    ChangeBatch={
        'Changes': [
            {
                'Action': 'UPSERT',
                'ResourceRecordSet': {
                    'Name': 'testwebserver.hands-on.cloud',
                    'ResourceRecords': [
                        {
                            'Value': '3.128.188.18',
                        },
                    ],
                    'TTL': 300,
                    'Type': 'A',
                },
            },
        ],
        'Comment': 'Web Server',
    },
    HostedZoneId='Z00594533FY3S68ROG6V2',
)
print(response)