gn_count= 0
exp_count = 0
olap_count = 0
not_olap_count = 0

#outlist_exp1= set()
#outlist_exp2 = set()
outlist_exp1 = []
outlist_exp2 = []

ele_set = set()

geneset_dict = {}
overlap_dict = {}
dicA = {}

with open('out_exp1.txt', 'w+') as out_1:
    with open('test_genesnames.txt', 'r+') as our_doc: #'genenames.txt'
        with open('test_exp.txt', 'r+') as exps: #'experiments.txt'
            file_doc = our_doc.read()
            file_exps = exps.readline()
            file_doc = file_doc.strip()
            file_doc = file_doc.split('\n')        
            file_exps = file_exps.strip()
            file_exps = file_exps.split('\n')
            #print('length file genenames', len(file_1))
            #print(file_1[0])
            #print('length file experiemt', len(file_2))
            #print(file_2)
            #print(file_1)
            #print(file_2)
            
            for gene_1 in file_doc:
                #gn_count += 1 
                #print(gene_1)  
                outlist_exp1.append(gene_1)
            #print (outlist_exp1)      
            
            
            for counter, gene_2 in enumerate(file_exps):               
                 
                #print(counter, gene_2)
                outlist_exp2.append(gene_2)
            print (counter, outlist_exp2)
               
                #geneset_dict[counter] = gene_2
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
                
                #print(int_ele)
                testset.append(list(int_ele))
            
            for counter, setset in enumerate(testset):   
                #print (counter, setset)    
                
                overlap_dict[counter] = setset
            #print (overlap_dict)
            
            for key, value in geneset_dict.items():
                dicA[str(value)] = overlap_dict[key]
                
            #print (dicA)
                
            
            
