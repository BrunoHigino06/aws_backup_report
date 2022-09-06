import csv
import yaml

with open(r'report.yaml', 'r') as file:
    data = file.read()
    data = data.replace("[]", "")

with open(r'report.yaml', 'w') as file:
    file.write(data)

fields = {
    'AccountId' : 'AccountId',
    'BackupJobId' : 'BackupJobId',
    'ResourceArn' : 'ResourceArn',
    'StartBy' : 'StartBy',
    'State' : 'State',
    'StatusMessage' : 'StatusMessage',
}

with open('report.csv', 'w', newline='') as f_output:
    csv_output = csv.DictWriter(f_output, fieldnames=fields.values())
    csv_output.writeheader()

    for filename in ['report.yaml']:
        with open(filename) as f_input:
            for row_yaml in yaml.safe_load(f_input):
                row_csv = {fields[key] : value for key, value in row_yaml.items()}
                csv_output.writerow(row_csv)