import sys
import glob 
from Bio import SeqIO


for name in glob.glob('*.fa.txt.pfa'):    
    print(name)
    name_no = name.split('.')
    #print(name_no[0])
    file_1 = open(name, 'r')
    #print(file_1)
    with open(('hmmscan-100_' + '%s' % (name_no[0]) + '.fasta' ), 'w+') as allwrite:
        my_record = list(SeqIO.parse(name, "fasta"))
        for i in range(0,100):
            print(i, my_record[i].id)
            print(my_record[i].seq)
            allwrite.write('>' + '%s\n%s\n' % (my_record[i].id, my_record[i].seq))

allwrite.close()
