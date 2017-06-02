########################################################################################3

#####DNA genome statistics tool, protein statistics tool
#####The results of applying your scripts to your genomes
#####Compute GC content and nucleotide (dinucleotide) frequency in a genome

from Bio.SeqUtils import GC
from Bio import SeqIO
import glob
import sys
import re
import string
import math 
import pylab

#################### Computing GC, Nucleotide and Dinulceotide frequency ###########################


	######## GC content count #########

def compute_gc(name):
    f1 = open(name, 'r')
    #print(f1)
    f1 = f1.read()
    #print(f1)   
    f1 = f1.split('\n')
    GC_content = GC(f1[1])
    print('GC content frequency')
    print(GC_content, '%')
	
	####### Dinucleotide count #######

    aa_count1 = len(re.findall('(?=AA)', str(f1[1])))
    ag_count1 = len(re.findall('(?=AG)', str(f1[1])))
    ac_count1 = len(re.findall('(?=AC)', str(f1[1])))
    at_count1 = len(re.findall('(?=AT)', str(f1[1])))
    ga_count1 = len(re.findall('(?=GA)', str(f1[1])))
    gg_count1 = len(re.findall('(?=GG)', str(f1[1])))
    gc_count1 = len(re.findall('(?=GC)', str(f1[1])))
    gt_count1 = len(re.findall('(?=GT)', str(f1[1])))
    ca_count1 = len(re.findall('(?=CA)', str(f1[1])))
    cg_count1 = len(re.findall('(?=CG)', str(f1[1])))
    cc_count1 = len(re.findall('(?=CC)', str(f1[1])))
    ct_count1 = len(re.findall('(?=CT)', str(f1[1])))
    ta_count1 = len(re.findall('(?=TA)', str(f1[1])))
    tg_count1 = len(re.findall('(?=TG)', str(f1[1])))
    tc_count1 = len(re.findall('(?=TC)', str(f1[1])))
    tt_count1 = len(re.findall('(?=TT)', str(f1[1])))

    total_DN1 = ag_count1 + gc_count1 + cc_count1 + ca_count1 + aa_count1 + ga_count1 + ac_count1 + gg_count1 +	ta_count1 + at_count1 + tg_count1 + gt_count1 + tc_count1 + ct_count1 + tt_count1
    
    print('\n')
    print('Dinucleotide Frequency')
    print('AA', (aa_count1/total_DN1)*100)
    print('AG', (ag_count1/total_DN1)*100)
    print('AC', (ac_count1/total_DN1)*100)
    print('AT', (at_count1/total_DN1)*100)
    print('GA', (ga_count1/total_DN1)*100)
    print('GC', (gc_count1/total_DN1)*100)
    print('GT', (gt_count1/total_DN1)*100)
    print('GG', (gg_count1/total_DN1)*100)
    print('CA', (ca_count1/total_DN1)*100)	
    print('CC', (cc_count1/total_DN1)*100)
    print('CT', (ct_count1/total_DN1)*100)
    print('CG', (cg_count1/total_DN1)*100)
    print('TA', (ta_count1/total_DN1)*100) 
    print('TG', (tg_count1/total_DN1)*100)
    print('TC', (tc_count1/total_DN1)*100)
    print('TT', (tt_count1/total_DN1)*100)
	
	####### Nucleotide count #######

    a_count = f1[1].count('A')
    g_count = f1[1].count('G')
    c_count = f1[1].count('C')
    t_count = f1[1].count('T')
    
    total_N = a_count + g_count + c_count + t_count
	
    print('\n')
    print('Nucleotide Frequency')
    print('A', (a_count/total_N)*100)
    print('G', (g_count/total_N)*100)
    print('C', (c_count/total_N)*100)
    print('T', (t_count/total_N)*100)	
    #print(total_N)

print(compute_gc((sys.argv [1])))
