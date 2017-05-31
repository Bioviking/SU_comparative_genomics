# this script takes the output of a blast run
# and outputs a fasta file with the best hit
# to the query in all database files where there is a hit
# as such, it makes sense only to use with single query sequences
# and mainly for databases that are genome files
# to find homologs to one or a set of genes in those genomes

import sys
import re
from Bio.Blast import NCBIXML

blastOutputXMLFile = sys.argv[1]
ref_tag = sys.argv[2]


blastOutputXMLHandle = open(blastOutputXMLFile)
#out_blast_records = open('output.fasta', "w")
#sys.stdout = out_blast_records

parser_output = open("output5_12.fa", "w")

listOfBlastRecords = NCBIXML.parse(blastOutputXMLHandle)

for aSingleBlastRecord in listOfBlastRecords:
	
		
	for i in range (len (aSingleBlastRecord.alignments)):
		if aSingleBlastRecord.query != []:	
			alignment = aSingleBlastRecord.alignments[0]
		

	parser_output.write('>' + aSingleBlastRecord.query + ' ')
	parser_output.write('>' + alignment.hit_def + '\n')
	#description = aSingleBlastRecord.descriptions[i]
	
	#title = re.compile ("gnl\|BL_ORD_ID\|\d* ").sub("", description.title)
	
	#	out_blast_records.write(">" + title + '\n')
	#	out_blast_records.write(alignment.hsps [0].sbjct + '\n')

parser_output.close()
