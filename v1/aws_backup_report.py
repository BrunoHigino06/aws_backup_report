import boto3, json, os

def aws_backup_report():
    date = "2022-09-05"
    status = "FAILED"
    regions = ["sa-east-1"]
    for region in regions:
        brute_data = os.system('aws backup list-backup-jobs --region '+region+' --by-created-afte '+date+' --output json --query "BackupJobs[*].{AccountId:AccountId,BackupJobId:BackupJobId,StartBy:StartBy,State:State,StatusMessage:StatusMessage,ResourceArn:ResourceArn}"')
        json_data = json.dumps(brute_data, indent=4, sort_keys=True, default=str)
        refined_data = json.loads(json_data)
        print(refined_data['AccountId'])

aws_backup_report()