######The ORFs predicted using your ORF predictor. Both show some statistics for them and show some examples#################
#how many?
#How many compared to the ones you got from GLIMMER/genscan?
#etc.


#Kozak seq
#Yeast -  	aAaAaAATGTCt
#####################Comput ORF############################


from Bio import SeqIO
from Bio.SeqUtils import six_frame_translations
import glob
import sys
import string
from Bio.SeqUtils import GC
import math 
import re


def comput_orf(name):
    f1 = open(name, 'r')
    f1 = f1.read()
    #print(f1)
    f1 = f1.split('\n')
    #print(f1[1])
    
    name = name.strip('.')
    name = name.split('/')
    name = name[3].split('.')
    print(name[0])
    
    #print(f1)
    #record = SeqIO.read(f1, "fasta")
    #table = 11
    #min_pro_len = 100
    
    
    with open('Trans_orf_pos_%s.fasta' % (name[0]), 'w+') as orf_write:
        print(six_frame_translations(f1[1]))
        orf_write.write('>%s.fasta\n %s' % (name[0], six_frame_translations(f1[1])))
    
'''    
    for strand, nuc in [(+1, record.seq), (-1, record.seq.reverse_complement())]:         
        #print(strand)
        #print(nuc)
        
        for frame in range(3):
            sign_frame = (frame+1) * strand
            #print(frame)
            #print(len(record)-frame)
            length = 3 * ((len(record)-frame) // 3) #Multiple of three from the start + the frame shift + length
            print(length)
            #seq_frame = str(nuc[frame:frame+length].translate(table, to_stop=True))
            #print(seq_frame[])
            for pro in nuc[frame:frame+length].translate(table).split("*"):   
                #count 
                if len(pro) >= min_pro_len:
                    print("%s...%s - length %i, strand %i, frame %i" % (pro[:30], pro[-3:], len(pro), strand, frame))
                    print('\n')
'''
'''                
#            for pro in nuc[frame:frame+length].translate(table).split("*"):                
                
                
                
                #for i in range(frame, frame+length, 3):
                #   print(i)
                #for pro in nuc[i:i+3].split("*"): #                 
                 #   print(pro)
                    
                    #if re.match('ATG')   
                #print(pro)
                #print('\n')
                
                #if len(pro) >= min_pro_len:
                    #print("%s...%s - length %i, strand %i, frame %i" 
                    #\ % (pro[:30], pro[-3:], len(pro), strand, frame))
    
    
    
    #print(six_frame_translations(f1[1]))

'''

for name in glob.glob('../data/grp7_genomes/*.fa.txt'):
    #print(name)
    print(comput_orf(name))
    
    
'''
>>> from Bio.Tools import Translate
>>> standard_translator = Translate.unambiguous_dna_by_id[1] 
>>> mito_translator = Translate.unambiguous_dna_by_id[2]

>>> standard_translator.translate_to_stop(my_seq)
'''

''' Rynos orf finder
            for m in re.finditer(r'ATG|GTG|TTG', seq_frame):   ###For translation start start site coordinates
                orf_count += 1
                orf_id = 'orf' + str(orf_count)
                print(orf_id) 
                print('%02d-%02d: %s %d' % (m.start(), m.end(), m.group(0), sign_frame))
'''

''' 
#record = SeqIO.read("NC_005816.fna", "fasta")
#table = 11
#min_pro_len = 100
for strand, nuc in [(+1, record.seq), (-1, record.seq.reverse_complement())]:
    for frame in range(3):
         length = 3 * ((len(record)-frame) // 3) #Multiple of three
         for pro in nuc[frame:frame+length].translate(table).split("*"):
             if len(pro) >= min_pro_len:
                 print("%s...%s - length %i, strand %i, frame %i" \
                       % (pro[:30], pro[-3:], len(pro), strand, frame))
'''
