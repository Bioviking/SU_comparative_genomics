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
    #print(f1)
    record = SeqIO.read(f1, "fasta")
    table = 11
    min_pro_len = 100
    max_thres = 40
    min_thres = 0
    orf_count = 0
    start_list = []
    end_list = []
    
    #s_codon = re.compile('ATG|GTG|TTG')    
    #e_codon = re.compile('TAG|TAA|TGA')
    for strand, nuc in [(+1, record.seq), (-1, record.seq.reverse_complement())]:         
        #print(strand)
        #print(nuc)
        
        for frame in range(3):
            sign_frame = (frame+1) * strand
            #print(frame)
            #print(len(record)-frame)
            length = 3 * ((len(record)-frame) // 3) #Multiple of three from the start + the frame shift + length
            #print(length)
            seq_frame = str(nuc[frame:frame+length]) #.translate(table, to_stop=True)
            #print(seq_frame[])
            for m in re.finditer(r'ATG|GTG|TTG', seq_frame):   ###For translation start site coordinate [AGT]TG [AGT](?=TG)
                start = m.start()
                print(start)
                start_list.append(start)
            for i in re.finditer(r'TAG|TAA|TGA', seq_frame):  ###For translation stop site coordinate (TA[AG]|T[AG]A) T(?=A[AG])|T(?=[AG]A)
                end = i.end() + 2
                print(end)
                end_list.append(end)                  
                print('%02d-%02d: %s %s %d' % (start, end, m.group(0), i.group(0),  sign_frame))    
            
            for s in start_list:
                #print(s)
                s = s + 2
                for e in end_list:
                #print(e)
                    if s < e:
                        diff_ms = e - s
                        #print(diff_ms)
                        if min_thres < diff_ms and diff_ms < max_thres: 
                            print(diff_ms)
                            #     orf_count += 1
                        #    orf_id = 'orf' + str(orf_count)
                          #  print(orf_id) 
                            print('%02d-%02d: %s %d' % (s, e, m.group(0), sign_frame))
'''   
    #print(record)
    #print(len(record.seq))
'''
#######TEST file ##########################3

name = 'test_seq.txt'

print(comput_orf(name))


#####################ROugh Stuff and Notes

'''             #######Possibly for the match of upstream of the translatiion site########3

### (?<=...)string is preceded by a match for ... that ends at the current position.            

'''


'''
for m in seq_frame:   ###For translation start site coordinate
                start= s_codon.search(seq_frame[m])
                print(start)
                #start = art()
                start_list.append(start)
            for i in seq_frame: ###For translation stop site coordinate
                end = e_codon.search(seq_frame[i])
                print(end[i])
                #end = i.end() + 2
                end_list.append(end)
                #s = s + 2
                
'''

'''
###############All the genomes#########################################
for name in glob.glob('../data/grp7_genomes/*.fa.txt'):
    #print(name)
    print(comput_orf(name))
'''    
    
'''##################Translate code###################################
>>> from Bio.Tools import Translate
>>> standard_translator = Translate.unambiguous_dna_by_id[1] 
>>> mito_translator = Translate.unambiguous_dna_by_id[2]

>>> standard_translator.translate_to_stop(my_seq)
'''


'''######################################Rynos orf finder##########################################
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



'''            
            if len(pro) >= min_pro_len:
                    print("%s...%s - length %i, strand %i, frame %i" % (pro[:30], pro[-3:], len(pro), strand, frame))
                    print('\n')
'''                    

'''            
            for pro in nuc[frame:frame+length].translate(table).split("*"):   
                count 
            
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
    
    #f1 = f1.read()
    #print(f1)
    #f1 = f1.split('\n')
    
    #print(six_frame_translations(f1[1]))

'''

