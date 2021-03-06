#!/usr/bin/env python2
#GC content calculator for a multifasta file
import re
import string
import sys
import os

def main():
	
	#Input file	
	input_file = sys.argv[1]
	
	# Check to make sure a valid filepath was specified
	if not os.path.isfile(input_file):
    		sys.exit("Invalid filepath specified!")
 
	#open the file   
	fp = open(input_file, 'r')

	contigNum = 0
	contigSeq = ""
	gcCount = 0

	for line in fp:
		if (line.startswith(">") and contigNum == 0):
			contigNum += 1
			
		elif (line.startswith(">")):
			gcCount = contigSeq.count("G") + contigSeq.count("C")
			gcPercent = 100*(float(gcCount)/len(contigSeq))
			print("Contig, %i, Length, %i, Percent GC, %f" % (contigNum, len(contigSeq),gcPercent))
			contigNum += 1
			gcCount = 0
			totalBaseCount = 0
			contigSeq = ""
		else:
			contigSeq = contigSeq + line.strip('\n')
			
			
main()
		
