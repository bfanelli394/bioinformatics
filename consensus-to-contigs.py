#!/usr/bin/env python2
#Consensus_to_contigs.py
#This script will take a consensus sequence in fasta form
#and split it into multiple contigs whenever a string of Ns appears
#
#Usage: python /path/to/consensus-to-contigs.py consensus_file.fa > output.fa

import string
import sys

def main():
	
	#create a consensus string of just one line from input file
	consensus = ''
	with open(sys.argv[1]) as f:
		for line in f:
			if not line.startswith(">"):
				consensus = consensus + line.strip('\n')
	
	contig = ''
	all_contigs = ''
	contig_num = 1 
	last_char = 'NULL' #Null only for first loop
	i=0
	
	while i < len(consensus): #iterate through the consensus string
	
		#if first char is an N, do nothing
		if (consensus[i] == 'N' and last_char == 'NULL'):
			pass
				
		#if N appears after last char was A,T,C,or G, write
		#contig to all_contigs, and reset the contig string	
		elif (consensus[i] == 'N' and last_char != 'N'):
			all_contigs += (">Contig_%s_len_%i" % (contig_num, len(contig)))
			all_contigs += '\n'
			all_contigs += contig
			all_contigs += '\n'
			all_contigs += '\n'
			contig = ''
			contig_num += 1 #increment to give unique name to each contig
		
		#if an N appears after another N, do nothing
		elif (consensus[i] == 'N' and last_char == 'N'):
			pass
			
		#Writes current base to contig string
		else:
			contig += consensus[i] 
		
		last_char = consensus[i] #record of last char for next iteration
		i += 1 #move to the next char in the consensus string
	
	#after the while loop, if the last char is not an N, this ensures 
	#that everything in contig is added to the all_contigs string
	if contig != '':
		all_contigs += (">Contig_%s_len_%i" % (contig_num, len(contig)))
		all_contigs += '\n'
		all_contigs += contig
	
	#print all contigs, will be in multifasta format		
	print all_contigs
	
	
main()
			
