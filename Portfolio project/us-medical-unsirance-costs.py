import csv
import matplotlib

# declaring list variables for CSV columns
age = []
sex = []
bmi = []
children = []
smoker = []
region = []
charges = []

# reading the CSV and parsing the columns to respective variables
with open('insurance.csv') as insurance_csv:
    insurance_data = csv.DictReader(insurance_csv)
    for item in insurance_data:
        age.append(item['age'])
        sex.append(item['sex'])
        bmi.append(item['bmi'])
        children.append(item['children'])
        smoker.append(item['smoker'])
        region.append(item['region'])
        charges.append(item['charges'])

# tidying data
for i in range(len(age)):
    age[i] = int(age[i])
    children[i] = int(children[i])
    bmi[i] = float(bmi[i])
    charges[i] = float(charges[i])


