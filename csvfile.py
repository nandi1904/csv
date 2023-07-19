import csv
import json

csv_file = 'county-info.csv'
json_file = 'county-info.json'

data = []
with open(csv_file, 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        data.append(dict(row))

with open(json_file, 'w') as file:
    json.dump(data, file, indent=4)

print("Conversion completed successfully.")