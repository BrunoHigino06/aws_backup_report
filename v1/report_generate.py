import json, boto3

def report_generate():
    print('AccountId,Account Name,Date')
    with open('./data.json') as json_file:
        database = json.load(json_file)

        for information in database['BackupJobs']:

            id = information['AccountId']
            organizations = boto3.client('organizations')
            org_response = organizations.describe_account(
                AccountId=id
            )
            org_json = json.dumps(org_response, indent=4, sort_keys=True, default=str)

            org_database = json.loads(org_json)

            #Colect account name
            accountname = org_database['Account']['Name']

            #Colect the start date
            startdate = information['CreationDate']

            print(id+','+accountname+','+startdate)







report_generate()