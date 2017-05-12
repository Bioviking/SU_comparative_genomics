import numpy as np
import matplotlib.pyplot as plt

def scatter(lab_A, lab_B):
    f_A = open(lab_A, 'r')
    f_B = open(lab_B, 'r')
    totaldict = dict()
    B_totaldict = dict()
    out_dict = dict()
    list3 =[]
    list4 =[]
    
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
        if C_key in B_totaldict.keys():
            list3.append(totaldict[C_key])
            list4.append(B_totaldict[C_key])
    
            
    print(len(list3))
    print(len(list4))
    plt.scatter(list3, list4) 
    plt.xlabel('Lab A')
    plt.ylabel('Lab B')
    plt.title('Scatter plot of Gene Expression')
    plt.show()
    
print(scatter('results_labA.dat', 'results_labB.dat')) 

'''            
    for C_key in totaldict.keys():
        if C_key in B_totaldict.keys():
            #out_dict[C_key] =  totaldict[C_key]
            list1.append(A_value)
            
    for outkey in B_totaldict.keys():
        if outkey in totaldict:
            #out_dict[outkey] = B_totaldict[outkey]    
            list1.append(B_value)
'''
