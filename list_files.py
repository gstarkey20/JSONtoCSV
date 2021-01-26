# This program is intended to look into a specific directory and locate 
# files with an .json extension. The file names will then be printed to 
# the console


import sys
import os


def list_files():
	entries = os.listdir('/Users/garrettstarkey/Desktop/PersonalProjects/JSONtoCSV')
	for entry in entries:
		print(entry)	

list_files()
