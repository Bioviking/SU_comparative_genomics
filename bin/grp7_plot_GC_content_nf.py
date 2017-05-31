import glob
import sys
import string
from Bio.SeqUtils import GC
import math 
from Bio import SeqIO
import pylab

'''
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
'''
########################PLot of GC%########################################
   
     
def plot_GC(GC_list):
    for file in GC_list:
        gc_values = sorted(GC(rec.seq) for rec in SeqIO.parse(file, "fasta"))
        print(file, gc_values)
            
 #gc_values = sorted(GC(rec.seq) for rec in SeqIO.parse("ls_orchid.fasta", "fasta")) 
    pylab.plot(gc_values)
    pylab.title("% orchid sequences\nGC%% %0.1f to %0.1f" \
                % (len(gc_values),min(gc_values),max(gc_values)))
    pylab.xlabel("Genes")
    pylab.ylabel("GC%")
    pylab.show()  


 

########################Read in genomes########################################
GC_list= []
for name in glob.glob('../data/grp7_genomes/*.fa.txt'):
    #print(name)
    GC_list.append(name)
    print(GC_list)
    
plot_GC(GC_list)
    
    #gc_values = sorted(GC(rec.seq) for rec in SeqIO.parse(f1, "fasta"))
   
    
    
    



    
