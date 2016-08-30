#!/usr/bin/env python2

# This script takes a reference sequence (previously used for an alignment)
# and prints the string again, incorporating gaps added in the alignment.
# For example, reference string ACTTGCATTGACGGAT and corresponding string
# in bam file of NNNN***NNN*NN**NNNNN**NN, output would be:
#
#    ACTT---GCA-TT--GACGG--AT
#    NNNN***NNN*NN**NNNNN**NN
#
# This allows for an easy comparison of the reference to a generated consensus sequence
#
# Usage: python ./pathto/Reference_includeGaps.py <N string file> <Referencefile>


import string
import os
import sys

def main():

	Nfile = sys.argv[1]
	
	#Reference should be in .txt format, not including a .fasta header line
	Reffile= sys.argv[2]
	
	refString = ''
	newRef = ''
	with open(Reffile) as f:
		for line in f: #Unwrap string of Ns
			refString = refString + line.strip('\n')
	Nstring = ''
	with open(Nfile) as g:
		for line in g: #Unwrap reference sequence
			Nstring = Nstring + line.strip('\n')
			
	i = 0
	j = 0
	
	while i < len(Nstring) and j < len(refString):
		
		#When a gap is not present, add the current reference base to the new reference
		#string, and move to the next position in both the reference and N string
		if Nstring[i] == "N":
			newRef = newRef + refString[j]
			i = i + 1
			j = j + 1
		
		#When a gap is present, add a dash to the new reference string, and only
		#iterate the N string file by one
		else:
			newRef = newRef + '-'
			i = i + 1
			
	#Print the new alignment of the two. After, concatenate this alignment with the 
	#generated consensus sequence
	print newRef
	print Nstring
			
main()
