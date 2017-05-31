#def save_unique(GN_list, experiments, output_filename):
r= open('genenames.txt', 'r')    
a= dict()
t= open('experiments.txt', 'r')   
b= dict()
f= open('overlapping_genesets', 'w')


#list of gene list
single = []   
for line in r:
	line=line.strip().split()       
	single.extend(line)


#list of experimental gene sets
set_list=[]        
for line in t:
	line=line.split()
	set_list.append(line)



# Find the overlapping genes between the GN list and each gene set	
c3 = [list(filter(lambda x: x in single, sublist)) for sublist in set_list]



#Dictionary between indexes and every gene set
sets_dict={}
for counter,position in enumerate(set_list):
	sets_dict[counter]=position



# Dictionary between index and every gene ID
match_dict={}
for counter, match in enumerate(c3):
	match_dict[counter]=match


# Merge dictionaries (Key= gene set, value= gene id of overlaped genes)
new_dict=dict()
for key,value in sets_dict.items():
	
	new_dict[str(value)]=match_dict[key]
#print(new_dict)


	
#lenght of values (=lenght of overlapping genes found)
supernew={}

for key,value in new_dict.items():

	supernew[key]=len(value)




#print the gene set with the highest number of overlapped genes
inverse = [(value, key) for key, value in supernew.items()]
print(max(inverse))
f.write(max(inverse)[1] + '\n')


#print the second gene set with the highest number of overlapped genes
del supernew[max(inverse)[1]]


inverse2 = [(value, key) for key, value in supernew.items()]
print(max(inverse2))
f.write(max(inverse2)[1])
f.close()



#c3.sort(key=len)
#print(c3)
#print(c3[-2:])

