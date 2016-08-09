#!/usr/bin/env python3
# HW05_ex09_01.py

# Write a program that reads words.txt and prints only the
# words with more than 20 characters (not counting whitespace).
##############################################################################
# Imports
import os

# Body
def path_setting():
	os.getcwd()
	os.chdir ("C:\\Users\\AJAY KUMAR PUTHIA\\Desktop\\Day 5\\D05")
	#This is the path setting function to be invoked only when used on Ankeet's Laptops. 
	#Other paths due to a different machine should be entered here and modified.



##############################################################################
def main():
	path_setting()

	file = open ("words.txt")
	arrays = file.read()
	array_list =arrays.split()
	total_words = len(array_list)

	print ("Total number of words is ", total_words)

	for x in array_list:
		length = len(x)
		if length >20:
			print (x)
			continue
		else:
			continue
	



    
if __name__ == '__main__':
    main()
