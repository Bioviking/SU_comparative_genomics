########################################################################################3
# 1. (*) Create a function that takes a string of nucleotids as input and returns its GC content as a number between 0 and 1. Call it compute_gc.
import glob
import sys
import string

def compute_gc(name):
    f1 = open(name, 'r')
    f1 = f1.read()
    
    count = 0
    total = 0
    g_dict = dict()
    for line in f1:
        line = line.strip()
        if line[0] == '>':
            line = line[1:]
            temp_id = line
            print(temp_id)
        else:
            for i in range(len(f1)):
                char = f1[i]
                if char == 'G' or char == 'C':
                    count += 1
            total = count / len(f1)     
            return total           
	

print()
print()
print('GC:')
for name in glob.glob('../data/grp7_genomes/*.fa.txt'):
        outfile = open('../results/GC_stat.txt', 'w+')
        outfile.write(compute_gc(name))
        

 
#outfile.write(print(compute_gc('')))
#print(compute_gc('AAACGTTGTGTTCCAAGGCTTGATATAGTCACGAT'))

#print()
#print()
