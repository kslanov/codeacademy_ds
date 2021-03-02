import csv

insurance_data = {}

with open('\Portfolio project\insurance.csv') as insurance_csv:
    read_csv = csv.DictReader(insurance_csv)
    print(read_csv)