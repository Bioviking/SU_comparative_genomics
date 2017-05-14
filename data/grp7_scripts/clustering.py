f1 = open("output5_9.fa", "r")
f2 = open("output5_11.fa", "r")
f3 = open("output5_12.fa", "r")

list_f1 = f1.readlines()
list_f2 = f2.readlines()
list_f3 = f3.readlines()

dict1 = dict() 
for element in list_f1:
	element = element.split()
	dict1[element[0]] = element[1]
	#print(dict1)

dict2 = dict()
for element in list_f2:
	element = element.split()
	dict2[element[0]] = element [1]
	#print(dict2)

dict3 = dict()
for element in list_f3:
	element = element.split()
	dict3[element[0]] = element [1] 
	#print(dict3)

#shit_output = open('orthologs', 'w')

key_dict1 = list(dict1.keys())
key_dict2 = list(dict2.keys())
key_dict3 = list(dict3.keys())

with open('orthologs', 'w') as ot:
	for eachkey in key_dict1:
		if (eachkey in key_dict2) and (eachkey in key_dict3):
			print ("This key %s exists in all dicts." % eachkey)
			ot.write("%s %s %s %s \n" %(eachkey, dict1[eachkey], dict2[eachkey], dict3[eachkey]))
