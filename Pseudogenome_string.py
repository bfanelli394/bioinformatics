#!/usr/bin/env python2
#This script is an edit of a sequence extractor script. It will create
#a genome file the length of a reference (7750108 is used here for Trichodesmium
#erythraeum and should be changed depending on the organism) including all sequences
#that created a blast hit and where they hit to the genome. All gaps are indicated
#as Ns
#
#Each line of the csv file started with a letter indicating which
#library/assembly the contig came from, so all 'if(row[2][0] == '[char]'):''
#should be changed depending on the context, as well as the print lines at
#the end of the script

import re
import string
import sys
import os
import csv
import itertools

def main():

	#CSV (BLAST) file
	fp = csv.reader(open(sys.argv[1], 'r'))
	#Contig file 1 - CW1
	contigs_1 = sys.argv[2]
	#Contig file 2 - Belize1
	contigs_2 = sys.argv[3]
	#Contig file 3 - FL2
	contigs_3 = sys.argv[4]
	#Contig file 4 - HB2
	contigs_4 = sys.argv[5]
	
	Cgenome_str = ''
	Bgenome_str = ''
	Fgenome_str = ''
	Hgenome_str = ''
	x = 1
	
	#Create 4 strings of all Ns
	while (x <= 7750108): #Tery genome is length 7750108
		Cgenome_str += 'N'
		Bgenome_str += 'N'
		Fgenome_str += 'N'
		Hgenome_str += 'N'
		x += 1
	
	for row in fp:

		#reset all strings aside from the genomes
		contig = ''
		sequence = ''
		temp = ''
		dir = ''
		
		#for nodes from the CW1 assembly
		if(row[2][0] == 'C'):
			#Define the direction of the sequence
			if(int(row[1]) < int(row[0])):
				dir = 'reverse'
			else:
				dir = 'forward'
		
			#lookup is node name from the second char
			#since the first is the lib identifier
			lookup = row[2][1:]
			for num, line in enumerate(open(contigs_1, 'r'), 1):
				if lookup in line:
					headerLn = num
			with open(contigs_1) as f:
				for i in xrange (headerLn):
					f.next()
				for line in f:
					if not line.startswith(">"):
						contig = contig + line.strip('\n')
					else:
						break
						
			if(dir == 'forward'):
				sequence = contig[int(row[3])-1:int(row[4])]
			else: #reverse compliment
				seq_dict = {'A':'T','T':'A','G':'C','C':'G'}
				temp = contig[int(row[3])-1:int(row[4])]
				sequence = "".join([seq_dict[base] for base in reversed(temp)])
			
			#Map the sequence to corresponding location in reference genome
			if(dir == 'forward'):
				Cgenome_str = Cgenome_str[:(int(row[0])-1)] + sequence + Cgenome_str[int(row[1]):]
			else:
				Cgenome_str = Cgenome_str[:(int(row[1])-1)] + sequence + Cgenome_str[int(row[0]):]
			
		
		#For nodes in the Belize1 assembly
		if(row[2][0] == 'B'):
			#Define the direction of the sequence
			if(int(row[1]) < int(row[0])):
				dir = 'reverse'
			else:
				dir = 'forward'
		
			#lookup is node name from the second char
			#since the first is the lib identifier
			lookup = row[2][1:]
			for num, line in enumerate(open(contigs_2, 'r'), 1):
				if lookup in line:
					headerLn = num
			with open(contigs_2) as f:
				for i in xrange (headerLn):
					f.next()
				for line in f:
					if not line.startswith(">"):
						contig = contig + line.strip('\n')
					else:
						break
			if(dir == 'forward'):
				sequence = contig[int(row[3])-1:int(row[4])]
			else:
				seq_dict = {'A':'T','T':'A','G':'C','C':'G'}
				temp = contig[int(row[3])-1:int(row[4])]
				sequence = "".join([seq_dict[base] for base in reversed(temp)])
			
			if(dir == 'forward'):
				Bgenome_str = Bgenome_str[:(int(row[0])-1)] + sequence + Bgenome_str[int(row[1]):]
			else:
				Bgenome_str = Bgenome_str[:(int(row[1])-1)] + sequence + Bgenome_str[int(row[0]):]
				
		#For nodes in the FL2 assembly
		if(row[2][0] == 'F'):
			#Define the direction of the sequence
			if(int(row[1]) < int(row[0])):
				dir = 'reverse'
			else:
				dir = 'forward'
		
			#lookup is node name from the second char
			#since the first is the lib identifier
			lookup = row[2][1:]
			for num, line in enumerate(open(contigs_3, 'r'), 1):
				if lookup in line:
					headerLn = num
			with open(contigs_3) as f:
				for i in xrange (headerLn):
					f.next()
				for line in f:
					if not line.startswith(">"):
						contig = contig + line.strip('\n')
					else:
						break
			if(dir == 'forward'):
				sequence = contig[int(row[3])-1:int(row[4])]
			else:
				seq_dict = {'A':'T','T':'A','G':'C','C':'G'}
				temp = contig[int(row[3])-1:int(row[4])]
				sequence = "".join([seq_dict[base] for base in reversed(temp)])
			
			if(dir == 'forward'):
				Fgenome_str = Fgenome_str[:(int(row[0])-1)] + sequence + Fgenome_str[int(row[1]):]
			else:
				Fgenome_str = Fgenome_str[:(int(row[1])-1)] + sequence + Fgenome_str[int(row[0]):]
				
		#For nodes from the HB2 assembly
		if(row[2][0] == 'H'):
			#Define the direction of the sequence
			if(int(row[1]) < int(row[0])):
				dir = 'reverse'
			else:
				dir = 'forward'
		
			#lookup is node name from the second char
			#since the first is the lib identifier
			lookup = row[2][1:]
			for num, line in enumerate(open(contigs_4, 'r'), 1):
				if lookup in line:
					headerLn = num
			with open(contigs_4) as f:
				for i in xrange (headerLn):
					f.next()
				for line in f:
					if not line.startswith(">"):
						contig = contig + line.strip('\n')
					else:
						break
			if(dir == 'forward'):
				sequence = contig[int(row[3])-1:int(row[4])]
			else:
				seq_dict = {'A':'T','T':'A','G':'C','C':'G'}
				temp = contig[int(row[3])-1:int(row[4])]
				sequence = "".join([seq_dict[base] for base in reversed(temp)])
			
			if(dir == 'forward'):
				Hgenome_str = Hgenome_str[:(int(row[0])-1)] + sequence + Hgenome_str[int(row[1]):]
			else:
				Hgenome_str = Hgenome_str[:(int(row[1])-1)] + sequence + Hgenome_str[int(row[0]):]
				
	print(">CW1_genome")
	print(Cgenome_str)
	print(">Belize1_genome")
	print(Bgenome_str)
	print(">FL2_genome")
	print(Fgenome_str)
	print(">HB2_genome")
	print(Hgenome_str)
	
			
		

main()
