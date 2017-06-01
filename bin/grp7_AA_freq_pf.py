###################################################################
#############

#####DNA genome statistics tool, protein statistics tool
#####The results of applying your scripts to your proteomes
#####compute amino acid (diamino acid) frequencies in a proteome
from Bio import SeqIO
import glob
from Bio.SeqUtils import ProtParam
from Bio.SeqUtils import ProtParamData
import sys
prot_seq =[]
pep_count = 0
for name in glob.glob('orf_pro_*.fasta'):
    #print(name)
    #print(name)
    f1 = open(name, 'r')
    
    
    
    f1=f1.readlines() 
    #print(f1)
    for i in range(1,len(f1),2):
        #print(f1[i])
        line= f1[i]
        line=line.strip('\n')
        prot_seq.append(line)
        #print(line)
        long_seq = ''.join(prot_seq)
           
    prot = ProtParam.ProteinAnalysis(long_seq)
    print(prot.count_amino_acids())
    print(prot.get_amino_acids_percent())
   
    
#    for i in prot.count_amino_acids():        
        
    #print(prot.get_amino_acids_percent())
'''        
        for i in prot.count_amino_acids():
            #print(i)
            print(prot.count_amino_acids())
            #print(prot.count_amino_acids[i])
            #print(key)
            
        sys.exit()
        #print(prot.molecular_weight())
        #print(prot.aromaticity())
        #print(prot.instability_index())
        #print(prot.flexibility())
        #print(prot.isoelectric_point())
        #print(prot.secondary_structure_fraction())
        #print(prot.protein_scale(ProtParamData.kd, 9, 0.4))
'''


'''           
        
        
        
        
        
        
   #     prot_seq.append(line)
    
    #for line in f1:
        #line= line.strip('')
        #line=line.strip(' \n')
        #line = line.split('\n')
        #print(line)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #line= str(line)
        #print(f1)
        #for i in len(line):   
         #   print(f1[0])
        
        
        
        #for i in line:
         #   print(i)
            #if line[0].startswith('>'):
             #   print(i)
                #pep_count+=1
                #id_list.append(line)
            #else:
             #   
    #for i in prot_seq:
        #print(i)
    #totalprot.join(i)       
            
        #x = ProteinAnalysis(line)  
                    
        
    #for line in f1:
     #   print(line[0])
    
'''    
    
    #   
    #print(f1)
    
   # for line in f1:
     #   print(line)
      #  print(line)
    #    line = line[1]
    #record = SeqIO.read(f1, "fasta")
    #
    #print(record)
    
    #f1 = f1.read()
    #print(f1)
    #
    #for line in f1:
     #   print(line)
        
#    f1= f1.strip()
    
 #   f1 = f1.split()
    
    #for i in f1[1]:
     #   print(i)
    
'''
    X = ProteinAnalysis("MAEGEITTFTALTEKFNLPPGNYKKPKLLYCSNGGHFLRILPDGTVDGTRDRSDQHIQLQLSAESVGEVYIKSTETGQYLAMDTSGLLYGSQTPSEECLFLERLEENHYNTYTSKKHAEKNWFVGLKKNGSCKRGPRTHYGQKAILFLPLPV")
print(X.count_amino_acids())
print(X.get_amino_acids_percent())
print(X.molecular_weight())
print(X.aromaticity())
print(X.instability_index())
print(X.flexibility())
print(X.isoelectric_point())
print(X.secondary_structure_fraction())
print(X.protein_scale(ProtParamData.kd, 9, 0.4))
'''    
