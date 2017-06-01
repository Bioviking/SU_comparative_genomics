######The ORFs predicted using your ORF predictor. Both show some statistics for them and show some examples#################
#how many?
#How many compared to the ones you got from GLIMMER/genscan?
#etc.


#Kozak seq
#Yeast -  	aAaAaAATGTCt
#####################Comput ORF############################


from Bio import SeqIO
from Bio.SeqUtils import six_frame_translations
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna
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
    min_pro_len = 30
    max_thres = 15000          #default to ?????
    min_thres = 100           #default to 100
    orf_count = 0
    start_list = []
    tata_list= []
    orf_seq = []
    
    #print(name)
    name = name.strip('.')
    name = name.split('/')
    name = name[3].split('.')
    print(name[0])
    
    
    tata_box = re.compile(r'TATA[ATC]{2}')   #eukaryotes and #prokaryotes
    #promoter = re.compile(r'TATAA[AT][AGCT]{8,45}')    
    enhancer = re.compile(r'TTGACA') #[ACTG]{26,38}([ACTG]{26,38})
    #sd_region = re.compile(r'[AG]{6,8}[ACTG]{3,10}')
    #yeast = re.complie('aAaAaAATGTCt')
    #e_coli = re.complie('')
    #codon_dict = {}
    s_codon = re.compile(r'([AGT]TG)')    
    e_codon = re.compile(r'(TA[AG]|T[AG]A)')
    with open('orf_seq_%s.fasta' % (name[0]), 'w+') as orf_write:
        with open('orf_pro_%s.fasta' % (name[0]), 'w+') as orf_pro_write:
            print('>%s' % (record.id))
            #orf_write.write('>%s\n' % (record.id))
             
            for strand, nuc in [(+1, record.seq), (-1, record.seq.reverse_complement())]:         
                #print(strand)
                #print(nuc)
                
                for frame in range(3):
                    sign_frame = (frame+1) * strand
                 #   print('Strand:', sign_frame)
                    #print(len(record)-frame)
                    length = 3 * ((len(record)-frame) // 3) #Multiple of three from the start + the frame shift + length
                    #print(length)
                    seq_frame = str(nuc[frame:frame+length]) #.translate(table, to_stop=True)
                    #print(seq_frame[])
                    
                    #For translation start site coordinate  For eukaryotes Kozak con_seq: '[GC]{3}[AG]CC([AGT]TG)G' for prokaryotes, Shine-Dalgarno seq:   extra: [AGT]TG or  [AGT](?=TG) or ^ATG[ATGC]{30,1000}A{5,10}$ or '(ATG|GTG|TTG)' 
                    ##################################Find TATA box################################################                                
                    for m in tata_box.finditer(seq_frame): #works ([AGT]TG)   yeast 'aAaAaAATGTCt' promoter : SDregion: [AG]{3,10}    
                        #if sd_region.search(m):
                        TSS_start = m.start()
                        up_seq = seq_frame[m.start()-120: m.end()]
                        down_seq = seq_frame[m.start() : m.end()+50]
                        
                        tata_list.append(TSS_start)
                        #print('is TSS:', TSS_start)
                        #print('is m: ' , m)
                        ################################Find upstream enhancer#################################
                        n = re.search(r'TTGACA', up_seq)                    #([ACTG]{26,38})
                        if n:                                               #from the start of the enhancer to the start of TATA box 
                            
                            usd= m.end() - (126 - n.start())                          #usd = upstream distance including the TATA box  
                            ms = m.start() - (126 - n.start())                        # upstream distance  excluding the TATA box
                            
                            #print('Enhancer and its postion is:', up_seq[n.start() ::], ms, m.end())                      
                            pos_pro2 = up_seq[n.start()::]
                            #print('Upstream promotor seq', pos_pro2)
                        ###########################Tranlation Start site##########################                        
                            
                            
                            o = s_codon.search(down_seq)
                            if o:                                       # for Seq_frame from end of TATA box to the end of the Trans Start codon                     
                                dsd = m.start() + o.end()               #dsd = downstream distance including the TATA box
                                os = m.end() + o.end()
                                pos_start = m.end() + o.start()                  # downstream distance excluding the TATA box      
                                diff_box2start =  (m.end() + o.start()) - m.end() 
                                
                                if diff_box2start > 15 and diff_box2start < 60:                  #minimun distance of the TATA box and the Start codon              
                                    
                                    #print('Enhancer:', 'Start:', n.start(), 'End:', n.end())
                                    #print('TATA:', 'Start:', m.start(), 'End:', m.end())
                                    #print('Start site:', 'Start:', o.start(), 'End:', o.end())
                                    
                                    #print('Up seq of TATA:', up_seq, m.start()-120)
                                    #print('Down seq of TATA:',down_seq, m.end()+50)                           
                                    #print('\n')
                                    
                                    ts_codon = down_seq[o.start() : o.end()]  
                                    
                                    #print('Enhancer to Tata:', up_seq[n.start():], ms, m.end())   
                                    #print('Distance:', diff_box2start)                                                      
                                    
                                    #print('Tata box to Trans start codon is:', down_seq[: o.end()])#????
                                                                
                                    #print('Translation start codon is:', ts_codon, o.start(), o.end(), 'Down_seq is length:', len(down_seq[:: o.end()])) 
                                    
                                    #print('Enhancer to Start codon', seq_frame[usd:dsd], ts_codon, usd, dsd) # Enhancer to Start codon, start codons, upstream distance, downstream distance                                
                                    first_stop = max_thres 
                                    for i in e_codon.finditer(seq_frame):  ###For translation stop site coordinate (TA[AG]|T[AG]A) T(?=A[AG])|T(?=[AG]A)                        
                                        diff_ms = i.start() - dsd 
                                        check_frame = diff_ms % 3
                                        if check_frame == 0:                                         
                                            if i.start() > dsd and min_thres < diff_ms and diff_ms < max_thres:
                                                if diff_ms < first_stop:                                                
                                                    first_stop = diff_ms
                                                    #print('For', i, 'Start',  i.start(), 'End', i.end())
                                                    #print('The is orf seq start start:', seq_frame[pos_start:i.end()])
                                                    start= dsd - 3
                                                    end = i.end()
                                                    orf_count += 1
                                                    orf_id = ('>%s_orf%s' % (name[0], str(orf_count)))                                                                                           
                                                    #print('%s %d %d %s - %s %d %dbp\n' % (orf_id, start, i.end(), o.group(0), i.group(0),  sign_frame, diff_ms))
                                                    #print(seq_frame[start:i.end()], '\n')        
                                                    orf_write.write('%s \n' % (orf_id))
                                                    orf_write.write(seq_frame[start:i.end()] + '\n')
                                                    #print('%s \n' % (orf_id))
                                                    orf_seq2 = str(seq_frame[start:end])
                                                    coding_dna = Seq(orf_seq2, generic_dna)
                                                    pro = coding_dna.translate(table, to_stop=True)
                                                    protein_lst.append(pro)
                                                    if len(pro) >= min_pro_len:               
                                                        print('%s \n' % (orf_id))
                                                        print(pro, '\n')
                                                        orf_pro_write.write('%s \n' % (orf_id))
                                                        orf_pro_write.write('%s\n' %(pro))
                
            
                                                            
    
    #for tide in orf_seq:                                                
     #   print(tide)
      #  length = len(orf_seq)
        #for pro in tide[1:length].translate(table):
         #   print(pro)
'''                                                    
                                                length = len(orf_seq)
                                                print(length)
                                                print(orf_seq)
'''
                                                #print(orf_seq.translate(table)) #.translate(table).split("*")
                                                    
                                                    
                                                  #  if len(pro) >= min_pro_len:                                                        
                                                   #     print('%s \n' % (orf_id))
                                                    #    print("%s - length %i \n" % (pro, len(pro)))
                                                                
                                                
                                                #orf_write.write(
                                                
                                                
            
                                        
                                        
                        
                        
                        #print('TTGACA & TATA?', seq_frame[pos_pro2:m.end()], len(seq_frame[pos_pro2:m.end()]))
                    #start_list.append(start)

'''                        
                        
                       
                        end_list.append(end)                  
                        if start < end:                               #Conditions for the length of the peptides on main data it will be not less than 100 
                            diff_ms = end - start
                            check_frame = diff_ms % 3
                            
                           # and diff_ms < short_orf
                            if check_frame == 0:                #Checking length divisable by 3 and in the right frame
                                short_orf = diff_ms
                                #print(diff_ms)
                                if min_thres < diff_ms and diff_ms < max_thres:    #checking the max and mininal threshold of the peptide sequence                                             
                                    orf_count += 1
                                    orf_id = 'orf' + str(orf_count)                                                                                           
                                    print('%s \t %d \t %d \t %s - %s \t %d %dbp\n' % (orf_id, start, end, m.group(0), i.group(0),  sign_frame, diff_ms))                                      
                                    orf_write.write('%s \t %d \t %d \t %s - %s \t %d %dbp\n' % (orf_id, start, end, m.group(0), i.group(0),  sign_frame, diff_ms))  
                    
'''
'''  
    print(record)
    print(len(record.seq))
'''
###Input#################TEST file ##########################3
'''
name = 'test_seq.txt'

print(comput_orf(name))
'''

###Input################The real deal multi glob glob genome predictor#######

###############All the genomes#########################################
for name in glob.glob('../data/grp7_genomes/*.fa.txt'):
    #print(name)
    print(comput_orf(name))
    

#####################ROugh Stuff and Notes

'''
#########################Previous length conditions with list###########3333
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
                ####????print('%02d-%02d: %s %d' % (s, e, m.group(0), sign_frame))???
'''


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

