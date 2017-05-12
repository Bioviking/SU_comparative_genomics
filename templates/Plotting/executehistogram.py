import numpy as np
import matplotlib.pyplot as plt


def histogram(lab_A, lab_B):
    f_A = open(lab_A, 'r')
    f_B = open(lab_B, 'r')
    list1 =[]
    list2 =[]
    list3 =[]
    
    for line in f_A:
        A_keyandvalue = line.strip().split()
        A_key = A_keyandvalue[0]
        A_value = float(A_keyandvalue[1])
        list1.append(A_value)       
       
    for B_line in f_B:
        B_keyandvalue = B_line.strip().split("," " ")
        B_key = B_keyandvalue[0]
        B_value = float(B_keyandvalue[1])
        list2.append(B_value)
       
    #print(list1)
    #print(list2)
    plt.hist(list1, 50, facecolor='r',histtype='step',label='Lab A') 
    plt.hist(list2, 50, facecolor='g',histtype='step',label='Lab B') 
    plt.xlabel('Gene Expression')
    plt.ylabel('Frequency')
    plt.title('Histogram of Gene Expression')
    plt.legend()
    plt.show()
    
print(histogram('results_labA.dat', 'results_labB.dat')) 


