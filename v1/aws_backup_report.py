import boto3, json, os

def aws_backup_report():
    date = "2022-09-05"
    status = "FAILED"
    regions = ["sa-east-1"]
    for region in regions:
        accountId = os.system('aws backup list-backup-jobs --region '+region+' --by-created-afte '+date+' --output text --query "BackupJobs[*].{AccountId:AccountId}"')
        for accountname in range(accountId):
            print('test: '+accountname)

aws_backup_report()