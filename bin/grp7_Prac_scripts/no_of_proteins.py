import sys
import glob

count = 0
count2 = 0
f1 = open('orthologs', 'r')
for line in f1:
    line = line.split('\n')
    if line[0].startswith('>'):
        count += 1
        
    else:       
        continue
print(count)
'''   
    if count > temp_count:
        temp_count = count
            
    else:
        continue
        
print(temp_count)
    
    #f1 = f1.readlines()

'''

