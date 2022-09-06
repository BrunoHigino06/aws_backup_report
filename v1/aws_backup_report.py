import boto3, json, os

def aws_backup_report():
    date = "2022-09-05"
    status = "FAILED"
    regions = ["us-east-1", "sa-east-1"]
    for region in regions:
        data = os.system('aws backup list-backup-jobs --region '+region+' --by-created-afte '+date+' --output json --query "BackupJobs[*].{AccountId:AccountId,BackupJobId:BackupJobId,StartBy:StartBy,State:State,StatusMessage:StatusMessage,ResourceArn:ResourceArn}"')
        print(data['BackupJobs']['AccountId'])

aws_backup_report()