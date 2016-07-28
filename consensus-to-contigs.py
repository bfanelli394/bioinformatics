#!/usr/bin/env python2
#Consensus_to_contigs.py
#This script will take a consensus sequence in fasta form
#and split contigs when a string longer than a specified length of Ns appear
#
#Usage: python /path/to/consensus-to-contigs.py <consensus_file.fa> <N-threshold>  > output.fa

import string
import sys

def main():
	
	#create a consensus string of just one line from input file
	consensus = ''
	with open(sys.argv[1]) as f:
		for line in f:
			if not line.startswith(">"):
				consensus = consensus + line.strip('\n')
	
	n_threshold = int(sys.argv[2]) #Max string of consecutive Ns allowed in contig
	
	contig = ''
	all_contigs = ''
	contig_num = 1 
	last_char = 'NULL' #Null only for first loop
	i=0
	next_thres_chars = ''
	n_compare = ''
	
	#Create a string, length of threshold + 1, of all Ns
    	for i in range(n_threshold+1):
    		n_compare += 'N'
	
	while i < (len(consensus)-n_threshold): #iterate through the consensus string
	
		#Create a string of the current base plus the next [N-threhold] base(s)
		for j in range(n_threshold+1):
			next_thres_chars += consensus[i+j]
				
		#if first char is an N, do nothing
		if (consensus[i] == 'N' and last_char == 'NULL'):
			pass
		
		#if string of [N-threshold] Ns appears after last char was A,T,C,or G, write
		#contig to all_contigs, and reset the contig string	
		elif (next_thres_chars == n_compare and last_char != 'N'):
			all_contigs += (">Contig_%s_len_%i" % (contig_num, len(contig)))
			all_contigs += '\n'
			all_contigs += contig
			all_contigs += '\n'
			all_contigs += '\n'
			contig = ''
			contig_num += 1 #increment to give unique name to each contig
		
		#if an N appears after another N, do nothing
		elif (next_thres_chars == n_compare and last_char == 'N'):
			pass
		
		#For Ns that appear after a contig split and before a new
		#contig is written, do nothing
		elif (consensus[i] == 'N' and contig == ''):
			pass
			
		#Writes current base to contig string
		else:
			contig += consensus[i] 
		
		last_char = consensus[i] #record of last char for next iteration
		
		next_thres_chars = '' #reset next chars string
		
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
			
