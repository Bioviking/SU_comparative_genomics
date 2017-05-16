import glob 
import sys


dict_seq = {}
list1 = []
list2 = []
dict_both = {}



f2 = open(sys.argv[1], 'r')
f2 = f2.read().split()
#print(f2)
for counter, seq  in enumerate(f2):
    #print('This is index', counter, seq)
    dict_seq[counter] = seq
    #print('is dict', dict_seq)
    #print(counter)

for name in glob.glob('geneOrder*.txt'):
    
    f1 = open(name, 'r')
    f1 = f1.readline().split(' ')
    #print(f1)
    list_ele = []
    print(name)
    print('\n')
    print('\n')
    #if dict_ele.keys() ==
    
    #else:
    for ele in f1:
        print(ele)
        #print('This is ele', ele)
        ele = int(ele)
        print(ele)
        list_ele.append(ele)
    #print(list_ele)
    
    #for i in list_ele:
        #print(dict_seq[i])
        #print(i)
        #dict_both[i] = 
        #list1.append(dict_seq[i])
        #list2 = ''.join(list1) 
    #print(list2)
    #dict_both[ele] = dict_seq.values()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    #print(dict_both)
        #dict_both.value[] = dict_seq.key(ele)
        
        
    #print(list2)
    #print(dict_both)
    #print(list2)    
        #print('is dict', dict_ele)
    #print(counter)
    
    #for i in list_ele:
        
        #print(i)
        #print('is list', list_ele[i])
        #print(dict_ele[D_keys])
        #print(ele)
        #dict_both[i] = dict_seq[ele]
        #print(dict_both)
        
        
        #for D_key2 in dict_seq.keys():
            #print(D_keys)
            #if 
                        
#        list1.append(dict_seq[D_key1])
#        list2 = ''.join(list1)    
            
    
    #print(dict_both)
#print(list1)
#print(list2)
#with open(('pseudo_'+name), 'w+') as pseudowrite:
#    pseudowrite.write( '%s\n%s' % (name, list2))
    
#pseudowrite.close()
