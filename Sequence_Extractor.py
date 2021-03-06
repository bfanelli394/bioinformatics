#!/usr/bin/env python2
#Returns sequences from a multifasta file
#This script is written to extract sequences of any length from a multifasta file.
#The way to use this script is $PATH/sequenceextractor.py [csv file] [contig file]. 
#Numbers are taken from the csv file under the assumption that column 1 is the sequence name,
#2 is the length, 8 and 9 are the start and end locations of the subject sequence, 5 is the
#query (contig) name, and columns 6 and 7 have the sequence start and end (to be extracted).
#This can be edited based on the job at hand and the layout of the csv file.
import re
import string
import sys
import os
import csv
import itertools

def main():
	
	
	#Node file
	node_file = sys.argv[2]

	#Open the csv file with nodes and sequence locations
	fp = csv.reader(open(sys.argv[1], 'r'))
	
	
	
	for row in fp:
		lookup = (row[4])
		dir = ''
		#Determine the directionality of the sequence
		if (int(row[6]) < int(row[5])):
			dir = 'reverse'
		else:
			dir = 'forward'
		print(">%s_len_%s_%s_%s_%s_%s_%s_%s" % ((row[0][4:40]), row[1], row[7], row[8], (row[4][:11]), dir, row[5], row[6]))
		for num, line in enumerate(open(node_file, 'r'), 1):
			if lookup in line:
				headerLn = num
		contig = ''
		sequence = ''
		temp = ''
		with open(node_file) as f:
			for i in xrange(headerLn):
				f.next()
			#create a contig string with no line breaks
			for line in f:
				if not line.startswith(">"):
					contig = contig + line.strip('\n')
				else:
					break
		#Extract sequence based on if it's forward or reverse. If reverse,
		#The reverse compliment is extracted and returned
		if (dir = 'forward'):
			sequence = contig[int(row[5])-1:int(row[6])-1]
		else:
			seq_dict = {'A':'T','T':'A','G':'C','C':'G'}
			temp = contig[int(row[6])-1:int(row[5])]
			sequence = "".join([seq_dict[base] for base in reversed(temp)])
		print sequence
		print " "
main()		
	
	
