#!/usr/bin/env python2
#This derivation of sequence_extractor.py extracts DNA sequences from multiple fasta files
#Locations of rows and files used can be changed based on organization of the .csv file
#Row parameter is to be specified, as the output will be the sequences of just one gene

import re
import string
import sys
import os
import csv
import itertools
import linecache

def main():

	#CSV file
	fp = csv.reader(open(sys.argv[1], 'r'))
	
	#Reference genome file
	ref_file = sys.argv[2]
	
	#Assembly file 1
	assem_1 = sys.argv[3]
	
	#Assembly file 2
	assem_2 = sys.argv[4]
	
	#Assembly file 3
	assem_3 = sys.argv[5]
	
	#Assembly file 4
	assem_4 = sys.argv[6]
	
	#Row (from csv) of gene to extract
	gene_row = sys.argv[7]
	
	i=0
	
	for row in fp:
		
		#initialize all strings
		dir = ''
		contig = ''
		sequence = ''
		temp = ''

		i += 1 #The current value of i will be the current row iterated
		if (i == int(sys.argv[7])):
		
			#1. extract from reference genome
			#check direction of the gene in reference genome
			if (int(row[5]) < int(row[4])):
				dir = 'reverse'
			else:
				dir = 'forward'
			print(">Tery_st_%s_end_%s_%s" % (row[4],row[5],dir))
			with open(ref_file) as f:
			#starting at line 2, construct a contig string
				for line in xrange(1):
					f.next()
				for line in f:
					contig = contig + line.strip('\n')
			if (dir == 'forward'):
				sequence = contig[int(row[4])-1:int(row[5])-1]
			else: #returns reverse compliment
				seq_dict = {'A':'T','T':'A','G':'C','C':'G'}
				temp = contig[int(row[5])-1:int(row[4])]
				sequence = "".join([seq_dict[base] for base in reversed(temp)])
			print sequence
			print " "
			
			#reset all strings. This is done after each sequence is printed
			contig = ''
			sequence = ''
			temp=''
			dir=''
			
			###
			###2. extract from first library
			###
			
			if (row[9] == ''): #direction will be 'none' if no values are present
				dir = 'none'
			elif (int(row[9]) < int(row[8])):
				dir = 'reverse'
			else:
				dir = 'forward'
			print(">%s_st_%s_end_%s_%s" % (row[7][0:15], row[8], row[9], dir))
			
			#lookup is used to determine where to start reading the contig file
			lookup = row[7] 
			for num, line in enumerate(open(assem_1, 'r'), 1):
				if lookup in line:
					headerLn = num
					
			with open(assem_1) as f:
				for i in xrange (headerLn):
					f.next()
				for line in f:
					if not line.startswith(">"):
						contig = contig + line.strip('\n')
					else:
						break
			if (dir == 'forward'):
				sequence = contig[int(row[8])-1:int(row[9])-1]
			elif (dir == 'reverse'):
				seq_dict = {'A':'T','T':'A','G':'C','C':'G'}
				temp = contig[int(row[9])-1:int(row[8])]
				sequence = "".join([seq_dict[base] for base in reversed(temp)])
			else:
				sequence = ''
			print sequence
			print " "
			contig = ''
			sequence = ''
			temp = ''
			dir = ''
			
			#3. extract from second library
			lookup = row[14]
			if (row[16] == ''):
				dir = 'none'
			elif (int(row[16]) < int(row[15])):
				dir = 'reverse'
			else:
				dir = 'forward'
			print(">%s_st_%s_end_%s_%s" % (row[14][0:15], row[15], row[16], dir))
			for num, line in enumerate(open(assem_2, 'r'), 1):
				if lookup in line:
					headerLn = num
			with open(assem_2) as f:
				for i in xrange (headerLn):
					f.next()
				for line in f:
					if not line.startswith(">"):
						contig = contig + line.strip('\n')
					else:
						break
			if (dir == 'forward'):
				sequence = contig[int(row[15])-1:int(row[16])-1]
			elif (dir == 'reverse'):
				seq_dict = {'A':'T','T':'A','G':'C','C':'G'}
				temp = contig[int(row[16])-1:int(row[15])]
				sequence = "".join([seq_dict[base] for base in reversed(temp)])
			else:
				sequence = ''
			print sequence
			print " "
			contig = ''
			sequence = ''
			temp = ''
			dir = ''
			
			
			#4. extract from third library
			lookup = row[22]
			if (row[24] == ''):
				dir = 'none'
			if (int(row[24]) < int(row[23])):
				dir = 'reverse'
			else:
				dir = 'forward'
			print(">%s_st_%s_end_%s_%s" % (row[22][0:15], row[23], row[24], dir))
			for num, line in enumerate(open(assem_3, 'r'), 1):
				if lookup in line:
					headerLn = num
			with open(assem_3) as f:
				for i in xrange (headerLn):
					f.next()
				for line in f:
					if not line.startswith(">"):
						contig = contig + line.strip('\n')
					else:
						break
			if (dir == 'forward'):
				sequence = contig[int(row[23])-1:int(row[24])-1]
			elif (dir == 'reverse'):
				seq_dict = {'A':'T','T':'A','G':'C','C':'G'}
				temp = contig[int(row[24])-1:int(row[23])]
				sequence = "".join([seq_dict[base] for base in reversed(temp)])
			else:
				sequence = ''
			print sequence
			print " "
			contig = ''
			sequence = ''
			temp = ''
			dir = ''
			
			#5. extract from fourth library
			lookup = row[30]
			if (row[32] == ''):
				dir = 'none'
			elif (int(row[32]) < int(row[31])):
				dir = 'reverse'
			else:
				dir = 'forward'
			print(">%s_st_%s_end_%s_%s" % (row[30][0:15], row[31], row[32], dir))
			for num, line in enumerate(open(assem_4, 'r'), 1):
				if lookup in line:
					headerLn = num
			with open(assem_4) as f:
				for i in xrange (headerLn):
					f.next()
				for line in f:
					if not line.startswith(">"):
						contig = contig + line.strip('\n')
					else:
						break
			if (dir == 'forward'):
				sequence = contig[int(row[31])-1:int(row[32])-1]
			elif (dir == 'reverse'):
				seq_dict = {'A':'T','T':'A','G':'C','C':'G'}
				temp = contig[int(row[32])-1:int(row[31])]
				sequence = "".join([seq_dict[base] for base in reversed(temp)])
			else:
				sequence = ''
			print sequence
			print " "
main()
			
			
			
