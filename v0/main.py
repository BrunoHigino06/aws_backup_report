import os

os.system('python3 aws_backup_report.py > report.yaml')
os.system('python3 yml_to_csv.py')