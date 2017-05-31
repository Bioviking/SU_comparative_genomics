

gn_count= 0
exp_count = 0
outlist_exp1= set()
outlist_exp2 = set()
all_olap = set()
ele_set = set()
geneset_dict = {}
overlap_dict = {}
olap_count = 0
not_olap_count = 0
max_len = 0
no2_len = 0
origset_dict = {}
with open('out_exp1.txt', 'w+') as out_1:
    with open('genenames.txt', 'r+') as our_doc: #'genenames.txt'
        with open('experiments.txt', 'r+') as exps: #'experiments.txt'
            file_1 = our_doc.read()
            file_2 = exps.read()
            file_1 = file_1.strip()
            file_1 = file_1.split('\n')        
            file_2 = file_2.strip()
            file_2 = file_2.split('\n')
            #print('length file genenames', len(file_1))
            #print(file_1[0])
            print('length file experiemt', len(file_2))
            #print(file_2)
            #print(file_1)
            #print(file_2)
            
            for gene_1 in file_1:
                #gn_count += 1 
                #print(gene_1)  
                outlist_exp1.add(gene_1)
                #print (outlist_exp1)      
            
            for counter, gene_2 in enumerate(file_2):               
                outlist_exp2.add(gene_2) 
                #print(counter, gene_2)              
                origset_dict[counter] = gene_2 # keys is the line no
                #print(outlist_exp2)
                #print(gene_2)  
            #print('\n')
            #print(origset_dict)
            #print(outlist_exp2.intersection(outlist_exp1))
            ele_list = []
            for counter, ele in enumerate(outlist_exp2):
                #print(ele)                
                geneset_dict[counter] = ele                
                ele_2 = ele.split()
                #print(ele_2)
                ele_set = set()
                temp_list = []
                for item in ele_2:
                    #print(item)                    
                    ele_set.add(item)
                    temp_list.append(item)
                
                #print(temp_list)
                ele_list.append(temp_list)
                #print(ele_set)               
            
            #print(ele_list) # Same order as genesset_dict
            #print(geneset_dict) #use value to get origset_dict key

                #print(ele_set.intersection(outlist_exp1))                               
                int_ele = ele_set.intersection(outlist_exp1)
                print(int_ele)
                for it in int_ele:
                    all_olap.add(it)
                print(len(all_olap))    
                #print(type(int_ele))
                
                len_set = len(int_ele)
                #print(len_set)
            #print(ele_list) # Same order as genesset_dict
            #print(geneset_dict) #use value to get origset_dict key

                if len_set > max_len:
                    max_len = len_set
                    max_gen = int_ele
                elif len_set <= max_len and len_set >= no2_len: 
                    no2_len = len_set
                    no2_gen = int_ele
                else:
                    pass
            print(len(all_olap))    
            #print(ele_list)        
            #print(geneset_dict)
           
            #print('Max length:',max_len)
            #print(max_gen)
            max_list= list(max_gen)
            #print('max list',max_list)
            #print('No2 length:', no2_len)
            #print(no2_gen)
            no2_list= list(no2_gen)
            #print('No2 list',no2_list)  
            i_count = 0

            for gen_set in ele_list:
                #set(gen_set)
                #print(gen_set)
                len_max = len(set(max_list).intersection(set(gen_set)))
                len_no2 = len(set(no2_list).intersection(set(gen_set)))
                #print(len_max)
                if max_len == len_max:
                    max_value = gen_set
                    #print('MAx set',gen_set)
                elif no2_len == len_no2:
                    no2_value = gen_set
                    #print('No2 set',gen_set)
                
                #print(len_max)
            #print(ele_list) # Same order as genesset_dict
            #print(geneset_dict) #use value to get origset_dict key
            
            #print('max value', max_value)
            max_value = ' '.join(max_value)
            print(max_value)
            out_1.write((max_value) + '\n')
            #print('no2 value', no2_value)
            no2_value = ' '.join(no2_value)
            print(no2_value)            
            #print(geneset_dict.values[max_value])
            out_1.write((no2_value) + '\n')



#######END#########        
#                for i in max_list:
                #for g_set in gen_set:
                    #print(g_set)
                    #
                     #     if i in gen_set:
                      #      i_count += 1
                   #     print(i_count)
                #if i == max_len:
                 #   print(gen_set)
                #for  in gen_set:
                 #   print('Yes')               
#                for i in max_list:
                      
                #out_1.write(str(int_ele) + '\n')
                #ele_list.append(int_ele)
                #print(int_ele)
                #testset.append(list(int_ele))
            #print(ele_list)
            
           # for counter, olap in enumerate(ele_list):   
             #   print (counter, olap)    
                
               # overlap_dict[counter] = olap
            #print (overlap_dict)
                  
               
                
'''                            
            max_ = ''
                                
            for i in ele_list:
                
                temp_len = len(i)
                if max_len < temp_len:
                    max_len = temp_len
                    max_ = i
            #print (max_)
            
            
           # for i in max_ :
                #if i in int_ele:
                    
                    #print(ele_set)
                
                    #print max_=
                    
                    #print('max', int_long)

                
                
                #def getSort (item):
                #    return len(item)
                    
                #sort_set = sorted(int_ele, key=getSort)
                #print(sort_set)
                #print(type(sort_set))
                
                
                
                #temp_len = len(int_ele)
                
                #sort_set = sorted(int_ele, key=len)
                #print(sort_set)
                
                #if temp_len > max_len:
                   #print(temp_len)
                
                
                
                
                                               
                #print(max_len)
                    #print(i)
                    #temp_len = len(i)
                    #print(temp_len)

                
                if temp_len > max_len:
                    max_len = temp_len
                    print(max_len)
                    #list.append(max_len)
                elif temp_len > no2_len:
                    no2_len = temp_len
                    print(no2_len)
                else:
                    pass
'''                                
                
                   
                
                
'''                
        with open('out_exp1.txt', 'w+') as out_1:
            for gn1 in outlist_exp1:
                
                olap_count += 1  
                
        with open('out_exp2.txt', 'w+') as out_2:
            for gn2 in outlist_exp2:
                out_2.write(gn2 + '\n')  
                not_olap_count += 1
'''        
        
        #print(ele_set)
        #print(outlist_exp1)
        #print(outlist_exp1.intersection(ele_set))

'''               
        print(len(outlist_exp1))
        
        print(len(outlist_exp2))
        

        print('Overlapping genes:', olap_count) 
        print('Not overlapping genes:', not_olap_count)

'''                  
                        #print(gene_1, gene_2)
        #        if gene_1 == gene_2:                
                    #print(gene_1, gene_2)
                                       
         #       elif gene_1 != gene_2:
                    
                #for item in outlist_exp1:
                 #   if gene_1 != item :             
