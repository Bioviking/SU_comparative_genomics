import sys
import glob
import string
from Bio.Blast import Record
from Bio import SeqIO

for fname in glob.glob('Cluster_*'): 
    count= 0
    print('This is the file %s' % (fname))
    with open(fname, 'r') as parsecluster:
        print('Parsecluster', parsecluster)
        for parsecluster in SeqIO.parse(parsecluster, "fasta"):
            print(parsecluster.id)
            for char in record.id:
            print(parsecluster.seq)
            
                print(record.id)
            #parsecluster = parsecluster.readlines()
            
            
            print('Is line', line)            
            if line.startswith('>'):
                line = line.split('_')
                print('Is splitline', line)
                if line[0] = '>./05fa.txt'):
                    print(line[0])
                if line[0] = '>./09fa.txt'):
                    print(line[0])
                if line[0] = '>./11fa.txt'):
                    print(line[0])
                if line[0] = '>./12fa.txt'):
                    print(line[0])
                else:
                    print("This is record sequence %s" % (record.seq))
                       # clustwrite.write('%s' % (record.seq))   
              
                    
            
            print('Parsecluster:', parsecluster)
        #parsecluster = SeqIO.parse(parsecluster, "fasta")
        print('this is each cluster', parsecluster[0])
            with open(("MultiG_"+ genome_id), 'w+') as clustwrite:    
                for line in clustwrite:                    
                    if line[0].startswith('./05'): 
                        print("This is record sequence %s" % (record.seq))
                        clustwrite.write('%s' % (record.seq))
                    else:
                        print("This is record %s" % (record))
                        print("This is record id %s" % (record.id))
                        clustwrite.write('%s\n' % (record.id))
                
for line in f1:
            line = line.rstrip('\n')
            print(line)
            if ':' in line:
                ele = line.split(':')
                print(ele)          
                if ele[0].startswith('11'): 
                    ele0 = 'Gsulfur'
                    #ele0 = ele[0].replace('Gsulfur')
                    outf1.write(ele0 + ':' + ele[1])
                if ele[0].startswith('09'): 
                    ele0 = 'Ecoli'
                    #ele0 = ele[0].replace('Ecoli')
                    outf1.write(ele0 + ':' + ele[1])
                if ele[0].startswith('05'): 
                    ele0 = 'Ctrach'
                    outf1.write(ele0 + ':' + ele[1])
                if ele[0].startswith('12'):                 
                    ele0 = 'Gviola'
                    outf1.write(ele0 + ':' + ele[1])
                if ele[0].startswith('0.000'): 
                    ele0 = ''
                    outf1.write(ele0 + ':' + ele[1])
            else:
                outf1.write(line)
                continue
        outf1.write('\n')        
	
	
	    
	    
	    
			
			
'''			
for i in file:
dictprot[i] = SeqIO.index(("Multigene_%s" %i), "fasta")
clusterFile = sys.argv[1]
record_dict = SeqIO.index(clusterFile, "fasta")
'''
