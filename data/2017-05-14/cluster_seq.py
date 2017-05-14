from Bio import SeqIO

dictprot05 = SeqIO.index("05.fa.txt.pfa", "fasta")
dictprot09 = SeqIO.index("09.fa.txt.pfa", "fasta")
dictprot11 = SeqIO.index("11.fa.txt.pfa", "fasta")
dictprot12 = SeqIO.index("12.fa.txt.pfa", "fasta")

print (dictprot05)
with open('orthologs', 'r') as orth:
	orth = orth.read().splitlines()
	count = 0
	for eachcluster in orth:
		cluster = eachcluster.split()
		with open(("Cluster_%s" %count), 'w+') as clustwrite:
			clustwrite.write((dictprot05.get_raw((cluster[0].lstrip('>'))).decode()))
			clustwrite.write((dictprot09.get_raw((cluster[1].lstrip('>'))).decode()))
			clustwrite.write((dictprot11.get_raw((cluster[2].lstrip('>'))).decode()))
			clustwrite.write((dictprot12.get_raw((cluster[3].lstrip('>'))).decode()))
		count += 1
		if count == 10:
			break
