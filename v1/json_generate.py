from sts_session import sts_session
from aws_backup_report import aws_backup_report

def json_generate():
    with open("accounts.txt") as f:
        for id in f:
            sts_session(id.strip())
            aws_backup_report()

json_generate()