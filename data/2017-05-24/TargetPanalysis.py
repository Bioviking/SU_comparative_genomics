# The input file is the output of the TargetP analyis

target = open('28_targetp')

lines=target.readlines()


y=0
total=0	
mito=0
mitolist=list()	
for protein in lines:
	if protein.startswith('.'): #Count the number of proteins
		prot=protein.split()
		total+=1
		
		if prot[5] == 'M': # Count the number of mitochondrial proteins and add the proteins into a list
			mito=+1
			mitolist.append(prot[0].replace('._','./')) #
#print mitolist		
print 'Fraction of predicted mitochondrial proteins:', (float(mito)/(total))*100, '%'

#The input file is the output of the phobius analysis

phobius=open('out_phob_28.fa.txt.pfa.txt')
plines=phobius.readlines()
msp=list()
for i in mitolist: # Select mitochondrial proteins with signal peptide and add them into a list
	#print i
	for phobprot in plines:
	    #print phobprot
	    if phobprot.startswith(i):
			if 'Y' in phobprot:
				a=phobprot.split('_')
								
				y+=1
				#print a[0]
				msp.append(a[1])
#print msp


print 'Predicted mitochondrial proteins with signal peptide:\n', '\n'.join(msp)
print 'Number of predicted mitochondrial proteins with signal peptide:', y
			 
