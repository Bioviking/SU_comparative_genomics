########################################################################################3
# 1. (*) Create a function that takes a string of nucleotids as input and returns its GC content as a number between 0 and 1. Call it compute_gc.
import glob
import sys
import string

def compute_gc(name):
    f1 = open(name, 'r')
    #print(f1)
    f1 = f1.read()
    f1 = f1.split('\n')
    print(f1[0])
    for char in f1[0]:
        print('1st char ', char)
        char = char.split()
        print('is char:', char)
        count = 0
        total = 0
        g_dict = dict()
        print(char[0])
        if char[0] == '>':
            print        
            char = char[1:]
            temp_id = char
            #print(temp_id)
        else:
            for i in range(len(f1)):
                char = f1[i]
                if char == 'G' or char == 'C':
                    count += 1
            total = count / len(f1)     
            return total
    print()
    print()
    print('GC:', total)
    outfile = open('../results/GC_stat.txt', 'w+')
    outfile.write('GC: %s' % (total))
    outfile.close()

for name in glob.glob('../data/grp7_genomes/*.fa.txt'):
    #print(name)
    compute_gc(name)
        

        

 
#outfile.write(print(compute_gc('')))
#print(compute_gc('AAACGTTGTGTTCCAAGGCTTGATATAGTCACGAT'))

#print()
#print()
