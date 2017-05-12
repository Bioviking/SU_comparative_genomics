#*) Two labs, A and B have performed experiments measuring gene expression for 500 genes each, where some of them overlap. Read both files (attached), and merge them in a single file like so: GreC 1.2 GreD 0.8 For the genes that both labs have measured, save the average. The order is irrelevant.
#(*) Same as before, but now save only the unique genes, that is, ignore the ones that were measured by both labs.
def merge_with_average(lab_A, lab_B, output_filename):
    f_A = open(lab_A, 'r')
    f_B = open(lab_B, 'r')
    o = open(output_filename, 'w')
    totaldict = dict()
    B_totaldict = dict()
    out_dict = dict()
    list1 =[]
    list2 =[]
    
    for line in f_A:
        A_keyandvalue = line.strip().split()
        A_key = A_keyandvalue[0]
        A_value = float(A_keyandvalue[1])
        if A_keyandvalue[0] in totaldict:
            totaldict[A_key] += A_value
        else:
            totaldict[A_key] = A_value
    
    for B_line in f_B:
        B_keyandvalue = B_line.strip().split("," " ")
        B_key = B_keyandvalue[0]
        B_value = float(B_keyandvalue[1])
        if B_keyandvalue[0] in B_totaldict:
            B_totaldict[B_key] += B_value
        else:
            B_totaldict[B_key] = B_value
    
    
    for C_key in totaldict.keys():
        list1.append(C_key)
        if C_key in B_totaldict.keys():
             list2.append(C_key)
             out_dict[C_key] = (totaldict[C_key] + B_totaldict[C_key])/2
        else:
            out_dict[C_key] =  totaldict[C_key]
        
        
        
                
                #elif B_key not in out_dict:
                #out_dict[C_key] += B_value      
             
    print(len(set(list2)))
    print(len(set(list1)))
    for outkey in B_totaldict.keys():
        if outkey not in out_dict:
            out_dict[outkey] = B_totaldict[outkey]
    
    for f_key in out_dict:
        o.write(f_key + ' ' + str(out_dict[f_key]) + '\n')
    
    #for B_outkey in B_totaldict:
    #    o.write(B_outkey + ' ' + str(B_totaldict[B_outkey]) + '\n')
    
    f_A.close()
    f_B.close()
    o.close()
    return output_filename
    print(out_dict)
    
print(merge_with_average('results_labA_small.dat', 'results_labB_small.dat', 'output_filename.dat'))  
