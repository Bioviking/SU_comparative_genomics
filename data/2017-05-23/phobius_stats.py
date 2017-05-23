import sys
import glob 
from Bio import SeqIO


for name in glob.glob('out_phob_*.txt'):
    record = {}
    total_TM = 0
    id_count = 0
    SP_count = 0
    zero_TM = 0
    file_1 = open(name, 'r')
    file_1 = file_1.read()
    file_1 = file_1.splitlines()  
    for ele in range(1, len(file_1)):
        #print(file_1[ele])
        line = file_1[ele].split()
        #print(line)
        for ele2 in line:
            print(ele2)           
            if ele2.startswith('.'):
                id_count+= 1
            elif line[0] > 0:
                print('Yes') 
            #    print(seq_id)
            #for tm_no in line[1]:
            #    print(tm_no)
            #for sp_count in line[2]:
            #    print(sp_count)
            
        print(id_count)    
'''            
            
            elif ele2.isdigit() == True:
                print('Yes')            
            #    ele2.type == int:
                i_ele2 = int(ele2)
                print(i_ele2)
            #elif line[(ele2)] > 0:
               # total_TM += int(line[ele])
            #elif line[ele2] == 0:
             #       zero_TM += 1
            #elif line[ele2] == 'Y':
             #   SP_count += 1
           
'''                                     

                
             
#       temp = ele.split()
       #print(temp)
       #print(title)
            #record[title(i)] = temp[ele]
            #print(record)
            #record[title[2]] = int(temp[1])
            #record[title[3]] = int(temp[2])
            #record[title[4]] = temp[3]
        #for entry in record:
         #    print(entry)
         #   title = file_1[]
          #  print(title)
        #print(file_1)
        #for ele in file_1:
         #   print(ele)
            
         #   print
