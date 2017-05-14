import sys
import glob
import re
import string

with open('edit', 'w+') as outf1:

    for name in glob.glob('belvu_outk_out_Cluster_*'):
        f1 = open(name, 'r')
        f1 = f1.readlines()
        for line in f1:
            line = line.rstrip('\n')
            print(line)
            if ':' in line:
                ele = line.split(':')
                print(ele)          
                if ele[0].startswith('11'): 
                    ele0 = 'Gsulfur'
                    #ele0 = ele[0].replace('Gsulfur')
                    outf1.write(ele0 + ':' + ele[1])
                if ele[0].startswith('09'): 
                    ele0 = 'Ecoli'
                    #ele0 = ele[0].replace('Ecoli')
                    outf1.write(ele0 + ':' + ele[1])
                if ele[0].startswith('05'): 
                    ele0 = 'Ctrach'
                    outf1.write(ele0 + ':' + ele[1])
                if ele[0].startswith('12'):                 
                    ele0 = 'Gviola'
                    outf1.write(ele0 + ':' + ele[1])
                if ele[0].startswith('0.000'): 
                    ele0 = ''
                    outf1.write(ele0 + ':' + ele[1])
            else:
                outf1.write(line)
                continue
        outf1.write('\n')        
            
                        


