import numpy as np
import matplotlib.pyplot as plt

link_count = 0
prot_count= 0

#######dictionarys
dict_prot = {}
dict_val = {}

######Sets
prot_set = set()

#####Lists
link_list = []
value_list = []
freq_list = []
x_node = []
y_prob =[]

with open('outdoc4932.txt', 'r+') as doc:
    file_1 = doc.read()
    
    file_1 = file_1.strip('\n')
    file_1 = file_1.split('\n')
    
    for i in file_1:
        
        i = i.split()
        
        link_list.append(i[0])
        prot_set.add(i[0])
    for i in link_list:
        link_count += 1
    for x in prot_set:
        prot_count += 1
    
    ave_con = link_count/prot_count
    #print(ave_con)
    temp_count = 0
    for prot in prot_set:
        temp_count = 0
        for prot2 in link_list:
            if prot == prot2:
                temp_count +=1
        dict_prot[prot] = temp_count     
        
        
    for values in dict_prot.values():
        #print(values) 
        node = values               
        #print(node)
        value_list.append(node)
        value_count = 0
        for item in value_list:          
            #print('is item', item)
            if node == item:
                value_count += 1
            #print(value_count)    
        dict_val[node] = value_count
        
    #print(dict_val)
    for keys, values in dict_val.items():
        #freq_int_no = values/prot_count
        #print(freq_int_no)
        x_node.append(keys)
        y_prob.append(values)
        #y_prob.append(freq_int_no)
        
    #print(x_node, y_prob)
    #for values in dict_val.values():
     #   print(values)

    for x, y in zip(x_node, y_prob):
        #print(x, y)
        log_valx = np.log10([x])
        log_valy = np.log10([y])
        #print(log_val)
        plt.scatter(log_valx, log_valy, color = 'yellow')
        plt.title('Saccharomyces cerevisiae')
        plt.xlabel('Node Degree')
        plt.ylabel('Frequency')
        
        #plt.log10(x, y, basex=np.e, basey=np.e)
    plt.show() 
    
    
    
    
 #       log_log = math.log10(freq_int_no)        
 #       freq_list.append(log_log)

  #  print(prot_count)
  #  print('it freq', freq_list)
    
    
    
    
    
       
    
    #node_count = dict_val[node]
    #print(node_count)

    
    #print(freq_int_no)
        
          
    
        
          #print(node)
            #print(dict_val[node], value_count)
            #node_count = dict_val[node]
        #else:
         #   pass
            #value_list.append(node)
            #value_count += 1
        
        
        
    #node_count = dict_val[node]
    #print(node_count)
    #freq_int_no = node_count/prot_count
    #print(freq_int_no)
    
        #freq_list.append(freq_int_no)
    #print(freq_list)
    
    
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
#        value_dict[values] = value_count
    
    #print(dict_prot) 
    #print(prot_set)
        #for ele in i:
            #print(ele[0])
            
        #file_1 = file_1.split('\n')
    
    #print(file_1)
    #for i in range(1,len(file_1)):
       #print(file_1[i])
     #  prot_set.add(file_1[i])
    #print(prot_set)    
        
        #prot = file_1[0]
    
    #protlist = protlist.append(prot)
    #print(protlist)
    
    #for line in file_1:
        #print(line)        
     #   line = line.split()
      #  print(line)
        #print(line[0])
        #prot = line[0]
        #print(prot)
        #print(protlist)
        #if prot in protlist:
         #   protlist = protlist.append(prot)
          #  print(protlist)
         #   prot_count +=1
          #  link_count += 1
        #elif line[0] in protlist:
         #   link_count += 1
    
    #ave_con = link_count/ prot_count
    #print(ave_con)
    #dict_prot[protein] = link_count
    
    #for protein in dict_protein:         
        #ave_con = dict_prot[protein]/ prot_count
        #dict_ave[protein] = ave_con 
'''
