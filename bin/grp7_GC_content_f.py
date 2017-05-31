########################################################################################3

#####DNA genome statistics tool, protein statistics tool
#####The results of applying your scripts to your genomes
#####Compute GC content and nucleotide (dinucleotide) frequency in a genome

import glob
import sys
import string
from Bio.SeqUtils import GC
import math 
from Bio import SeqIO
import pylab

########################Computing GC and Dinulceotide frequency########################################
def compute_gc(name):
    f1 = open(name, 'r')
    #print(f1)
    f1 = f1.read()
    #print(f1)   
    f1 = f1.split('\n')
    print(GC(f1[1]), '%')
    ag_count = f1[1].count('AG')
    gc_count = f1[1].count('GC')
    cc_count = f1[1].count('CC')
    ca_count = f1[1].count('CA')
    aa_count = f1[1].count('AA')
    ga_count = f1[1].count('GA')
    ac_count = f1[1].count('AC')
    total_N = ag_count + gc_count + cc_count + ca_count + aa_count + ga_count + ac_count     
    print('AG', (ag_count/total_N) *100)
    print('GC', (gc_count/total_N)*100)
    print('CC', (cc_count/total_N)*100)
    print('CA', (ca_count/total_N)*100)
    print('AA', (aa_count/total_N)*100)
    print('GA', (ga_count/total_N)*100)
    print('AC', (ac_count/total_N)*100)
    #total_N = ag_count + gc_count + cc_count + ca_count + aa_count + ga_count + ac_count
    print(total_N)
########################PLot of GC%########################################
   
     
    

 

########################Read in genomes########################################
for name in glob.glob('../data/grp7_genomes/*.fa.txt'):
    #print(name)
    print(compute_gc(name))

'''
gc_values = sorted(GC(rec.seq) for rec in SeqIO.parse(f1, "fasta"))
#print(gc_values)
 #gc_values = sorted(GC(rec.seq) for rec in SeqIO.parse("ls_orchid.fasta", "fasta")) 
    pylab.plot(gc_values)
    pylab.title("% orchid sequences\nGC%% %0.1f to %0.1f" \
                % (len(gc_values),min(gc_values),max(gc_values)))
    pylab.xlabel("Genes")
    pylab.ylabel("GC%")
    pylab.show()  
'''
    

        
'''
    for char in f1[0]:
        print('1st char ', char)
        char = char.split()
        print('is char:', char)
        G_count = 0
        C_count = 0
        total = 0
        g_dict = dict()
        print(char[0])
        if char[0] == '>':
                   
            char = char[1:]
            
            temp_id = char
            #print(temp_id)
        else:
            for i in range(len(f1)):
                
                char = f1[i]
                print(char)
                if char == 'G':              
                    G_count += 1
                elif char == 'C':
                    C_count += 1
            GC_total = C_count + G_count
            
            total = GC_total / len(f1)     
        print('No of Gs', G_count, 'No of Cs', C_count)
        return total

    print()
    print()
    print('GC:', total)
    outfile = open('../results/GC_stat.txt', 'w+')
    outfile.write('GC: %s' % (total))
    outfile.close()
'''
 
#outfile.write(print(compute_gc('')))
#print(compute_gc('AAACGTTGTGTTCCAAGGCTTGATATAGTCACGAT'))

#print()
#print()
