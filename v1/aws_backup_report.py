import boto3, json, os

def aws_backup_report():
    date = "2022-09-05"
    status = "FAILED"
    regions = ["sa-east-1"]
    for region in regions:
        accountId = os.system('aws backup list-backup-jobs --region '+region+' --by-created-afte '+date+' --output text --query "BackupJobs[*].{AccountId:AccountId}"')
        for accountname in accountId:

            organizations = boto3.client('organizations')

            org_response = organizations.describe_account(
            AccountId=accountId
            )

            org_json = json.dumps(org_response, indent=4, sort_keys=True, default=str)

            org_database = json.loads(org_json)

            accountname = org_database['Account']['Name']
            print(accountname)

aws_backup_report()