

gn_count= 0
exp_count = 0
outlist_exp1= set()
outlist_exp2 = set()
ele_set = set()
geneset_dict = {}
over_genes = {}
olap_count = 0
not_olap_count = 0

with open('out_exp1.txt', 'w+') as out_1:
    with open('test_genesnames.txt', 'r+') as our_doc: #'genenames.txt'
        with open('test_exp.txt', 'r+') as exps: #'experiments.txt'
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
               
                geneset_dict[counter] = gene_2
                #print(outlist_exp2)
                #print(gene_2)
            #print(geneset_dict[1])    
            
           
            testset = []
            for ele in outlist_exp2:
                #print(ele)                
                ele_2 = ele.split()
                #print(ele_2)
                ele_set = set()
                for item in ele_2:
                    #print(item)
                    ele_set.add(item)
                #print(ele_set)

                #print(ele_set.intersection(outlist_exp1))                               
                int_ele = ele_set.intersection(outlist_exp1)
                out_1.write(str(int_ele) + '\n')
                #ele_list.append(int_ele)
                print(int_ele)
                testset.append(list(int_ele))
            
            for counter, setset in enumerate(testset):
                   
                print (counter, setset)    
                    #over_genes[counter] = ele3
                #print (over_genes)
                    
                #print('I am', int_ele)
                
'''            max_len = 0
            no2_len = 0                
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
