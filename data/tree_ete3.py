from ete3 import NCBITaxa
import inspect
import re

ncbi = NCBITaxa()
#ncbi.update_taxonomy_database()

with open('outdoc243231.txt', 'r+') as doc:
    file_1 = doc.read()
    #print(file_1)
    file_1 = file_1.split('\n')
    #print(file_1)
    for line in file_1:
        #print(line)
        match = re.match('243231', line)
        #print(match)              
        if match:
            taxid2name = ncbi.get_taxid_translator(match)
            print(taxid2name)
         #   doc.write(line.replace(match, taxid2name))
          #  print(line)
#    taxid2name = ncbi.get_taxid_translator([4932, 243231, 251221, 362663, 272561])
    #print(taxid2name)
'''
    protlist = []
    link_count = 0
    prot_count= 0
    if protein not in protlist:
        protlist = protlist.append(protein)
        prot_count +=1
        link_count = 0
    elif protein in protlist:
        link_count += 1
    
    ave_con = link_count/ prot_count
    #dict_prot[protein] = link_count
    
    #for protein in dict_protein:         
        ave_con = dict_prot[protein]/ prot_count
        dict_ave[protein] = ave_con 


# {9443: u'Primates', 9606: u'Homo sapiens'}
#print([x[0] for x in inspect.getmembers(ete3, inspect.isclass) if x[0].endswith('Tree')])

'''
