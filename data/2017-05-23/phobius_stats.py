import sys
import glob 
from Bio import SeqIO
import numpy as np
import matplotlib.pyplot as plt

x_frac = []    
y_ave = []
for name in glob.glob('out_phob_*.txt'):
    record = {}
    total_TM = 0
    id_count = 0
    great_TM = 0
    SP_count = 0
    zero_TM = 0
    file_1 = open(name, 'r')
    file_1 = file_1.read()
    file_1 = file_1.splitlines()  
    for ele in range(1, len(file_1)):
        #print(file_1[ele])
        line = file_1[ele].split()
        #print(line)
        #print(line)
        if line[0]:
            id_count+= 1
        
        if line[1] == '0':
            zero_TM += 1
   
        if line[1] != '0':
            great_TM += 1
            i_ele = int(line[1])
            total_TM += i_ele
            
        if line[2] == 'Y':
            SP_count += 1   

    frac_zero = zero_TM/id_count
    frac_great = great_TM/id_count #Fract of TM protein = x
    ave_TM = total_TM/great_TM      #Ave number of TM segment = y
    frac_SP = SP_count/great_TM
      
    print(name)    
    print('TM zero', frac_zero)
    print('TM greater', frac_great)
    print('TM average', ave_TM)
    print('TM SP', frac_SP)
    print('\n')
    
#for frac_great, ave_TM in name:
          
    colors = ['b', 'c', 'y', 'm', 'r']

    

    x_frac.append(frac_great)
    y_ave.append(ave_TM)


lo0 = plt.scatter(x_frac[0], y_ave[0], color=colors[0])
lo1 = plt.scatter(x_frac[1], y_ave[1], color=colors[1])
lo2 = plt.scatter(x_frac[2], y_ave[2], color=colors[2])
lo3 = plt.scatter(x_frac[3], y_ave[3], color=colors[3])
lo4 = plt.scatter(x_frac[4], y_ave[4], color=colors[4])
plt.ylim(0,8)
plt.show()
'''
ll = plt.scatter(random(10), random(10), marker='o', color=colors[0])
l  = plt.scatter(random(10), random(10), marker='o', color=colors[1])
a  = plt.scatter(random(10), random(10), marker='o', color=colors[2])
h  = plt.scatter(random(10), random(10), marker='o', color=colors[3])
hh = plt.scatter(random(10), random(10), marker='o', color=colors[4])
ho = plt.scatter(random(10), random(10), marker='x', color=colors[4])
'''
'''
plt.legend((lo, ll, l, a, h, hh, ho),
           ('Low Outlier', 'LoLo', 'Lo', 'Average', 'Hi', 'HiHi', 'High Outlier'),
           scatterpoints=1,
           loc='lower left',
           ncol=3,
           fontsize=8)
'''
    
    
#def scatter(frac_great, ave_TM):
        
   
#N = 50
#x = np.array(frac_great)
#y = np.array(ave_TM)
#colors = np.random.rand(N)
#area = np.pi * (15 * np.random.rand(N))**2  # 0 to 15 point radii

#    plt.scatter(frac_great, ave_TM, color= 'r')
#plt.show()

