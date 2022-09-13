import json

def report_generate():
    with open('./data.json') as json_file:
        database = json.load(json_file)

        for AccountId in database['BackupJobs']:

            id = AccountId['AccountId']
            organizations = boto3.client('organizations')
            org_response = organizations.describe_account(
                AccountId=id
            )
            org_json = json.dumps(org_response, indent=4, sort_keys=True, default=str)

            org_database = json.loads(org_json)

            accountname = org_database['Account']['Name']

            print(accountname)





report_generate()