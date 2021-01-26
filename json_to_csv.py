# This program is intended to convert from JSON format to CSV format.

import sys
import os


def json_to_csv():
	entries = os.listdir('/Users/garrettstarkey/Desktop/PersonalProjects/JSONtoCSV')
	for entry in entries:
		print(entry)	

json_to_csv()
