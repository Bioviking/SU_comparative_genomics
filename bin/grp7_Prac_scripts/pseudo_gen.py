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

with open(('pseudo_all.txt'), 'w+') as allwrite:
    for name in glob.glob('geneOrder*.txt'):    
        print(name)
        f1 = open(name, 'r')

        
        list_ele = []
        seq_list = []
        join_list = []
        
        for line in f1:
            line = line.split(' ')
            #print(line)
            for ele in line:
                ele = int(ele)
                #print(ele)
                list_ele.append(ele)
            #print(list_ele)
            for i_ele in list_ele:
                #print(dict_seq[])
                #print(i_ele, dict_seq[i_ele])
                if i_ele in dict_seq.keys():
                    dict_both[i_ele] = dict_seq[i_ele]
                    #print(dict_both[i_ele])
                    seq_list.append(dict_both[i_ele])
                    join_list =  ''.join(seq_list)
                #print(seq_list)
            print(join_list) 
        with open(('pseudo_'+name), 'w+') as pseudowrite:
            pseudowrite.write('>pseudo' + '%s\n%s' % (name, join_list))         

        allwrite.write('>pseudo' + '%s\n%s\n' % (name, join_list))
#print(list1)
#print(list2)
#
    
pseudowrite.close()
allwrite.close()
