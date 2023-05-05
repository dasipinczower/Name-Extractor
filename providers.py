import json
import csv

# Open the JSON file for reading
with open('example.json', 'r') as json_file:
    # Load the JSON data into a Python dictionary
    data = json.load(json_file)

# Extract all the values with the key "name"
names = [item['name'] for item in data['items']]

# Open the CSV file for writing
with open('names.csv', 'w', newline='') as csv_file:
    # Create a CSV writer object
    writer = csv.writer(csv_file)

    # Write the header row
    writer.writerow(['Name'])

    # Write the name values to the CSV file
    for name in names:
        writer.writerow([name])
