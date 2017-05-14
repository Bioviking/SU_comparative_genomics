import sys
import glob
from Bio.Blast import Record
from Bio import SeqIO
filelist = []
for name in glob.glob('Cluster_*'):
    filelist.append(name)
    filelist.sort()

for file in filelist:
    dictcluster = SeqIO.parse(file, "fasta")
    print(file)
    for record in dictcluster:
        print("This is record %s" % (record)
        print("This is record %s" % (record.id)
        print("This is record %s" % (record.seq)



	#cluster = eachcluster.split()
	with open(("Multigene_0"), 'w+') as clustwrite:
	    clustwrite.write(record.id)
	    clustwrite.write(record.sequence)
	    clustwrite.write((dictcluster0.get_raw((cluster.lstrip('>'))).decode()))
			
			
'''			
for i in file:
dictprot[i] = SeqIO.index(("Multigene_%s" %i), "fasta")
clusterFile = sys.argv[1]
record_dict = SeqIO.index(clusterFile, "fasta")
'''
