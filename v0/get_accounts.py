#Function to colect all the AWS account ID and save an 
import json
import os
import logging

def get_accounts():

    # API call to get all informations about the accounts in the organization and save in a json file
    logging.info('Creating the json file with all account in the organization')
    os.system('aws organizations list-accounts >> organization.json')

    with open('organization.json') as json_file:
        database = json.load(json_file)

    for accountId in database['Accounts']:
        print(accountId['Id'])

get_accounts()
logging.info('Creating the txt file with all account IDs in the organization')
# Creating the txt file with all account IDs in the organization
os.system('py get_accounts.py > accounts.txt')
