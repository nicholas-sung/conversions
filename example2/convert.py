#!/usr/bin/env python3

import json
import csv

# use json.load to load input.json. load it into a variable called 'data'
with open('input.json', 'r') as f:
    data = json.load(f)

# use open to open 'output.csv' in write mode
with open('output.csv', 'w') as f:

# use csv.writer to create writer using the opened file
	writer = csv.writer(f)

# write the header of the csv
	writer.writerow(['id', 'value'])

# loop through the top level children data['children']
	for i in data['children']:
		print(i)
# use writer.writerow to write one row at a time with the name and budget


# - prepend 'flare.other.' to each name
# - remove any spaces in the name
