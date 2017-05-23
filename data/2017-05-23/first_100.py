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
            
            
            #
         #   for seq_record in my_record:
          #      print(myreseq_record[0].id)
                
#                print("%i %s" % (index, seq_record))
 #               print(my_record[:100]) #last letter
            #
             #   print()
                
                #print(seq_record)
                #for seq_record in SeqIO.parse(name, "fasta")):
                 #   print
                 #   print('this is', counter, seq_record.id)
                
            #for counter in range(0,100):
                
                #print(seq_record)
                #print(repr(seq_record.seq))
                #print(len(seq_record))
            
            

