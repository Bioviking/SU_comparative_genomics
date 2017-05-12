#14. (*) Remember the gene expression data from the previous session. In one single figure, plot the histogram of values for each lab so that both are visible. In a second figure, make a scatter plot of the ones in common comparing the values of each lab. Remember to label the axis. Submit the figure as an attachment. You do not need to submit the code.
import numpy as np

#data = np.loadtxt('')
data = np.loadtxt('results_labA_small.dat')
data
import matplotlib.pyplot as plt


import matplotlib.pyplot as plt
plt.plot([1,2,3,4])
plt.ylabel('some numbers')
plt.show()
###########################################MAINCODE##################################33

import numpy as np
import matplotlib.pyplot as plt


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
            list1.append(A_value)
       
    
    for B_line in f_B:
        B_keyandvalue = B_line.strip().split("," " ")
        B_key = B_keyandvalue[0]
        B_value = float(B_keyandvalue[1])
        if B_keyandvalue[0] in B_totaldict:
            B_totaldict[B_key] += B_value
            list2.append(B_value)
    
    plt.hist(list1, 50, normed=1, facecolor='r', alpha=0.75) 
    plt.hist(list2, 50, normed=1, facecolor='g', alpha=0.75) 
    plt.xlabel('Gene')
    plt.ylabel('Gene Expression')
    plt.title('Histogram of Gene Expression')
    plt.show()
    
    
    
    
    #histogram reference

    import numpy as np
    import matplotlib.pyplot as plt

    # Fixing random state for reproducibility
    np.random.seed(19680801)

    mu, sigma = 100, 15
    x = mu + sigma * np.random.randn(10000)

    # the histogram of the data
    n, bins, patches = plt.hist(x, 50, normed=1, facecolor='g', alpha=0.75)


    
    plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
    plt.axis([40, 160, 0, 0.03])
    plt.grid(True)
    plt.show()












#############################################################################        
'''
    for C_key in totaldict.keys():
        list1.append(C_key)
        if C_key in B_totaldict.keys():
             list2.append(C_key)
             out_dict[C_key] = (totaldict[C_key] + B_totaldict[C_key])/2
        else:
            out_dict[C_key] =  totaldict[C_key]
'''        
    
    
    
    for C_value in totaldict.value():
        list1.append(C_value)
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


###########################################################

#histogram reference

import numpy as np
import matplotlib.pyplot as plt

# Fixing random state for reproducibility
np.random.seed(19680801)

mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

# the histogram of the data
n, bins, patches = plt.hist(x, 50, normed=1, facecolor='g', alpha=0.75)


plt.xlabel('Gene')
plt.ylabel('Gene Expression')
plt.title('Histogram of Gene Expression')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()
