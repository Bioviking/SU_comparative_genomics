import sys, re

# acquire first needed data

geneOrderList = []

aHandle = open (sys.argv [1])

lines = aHandle.readlines ()

for aLine in lines:
    
    aLine = aLine.replace ("\n", "")

    if aLine.startswith (">"):
        
        print aLine [0:len (aLine)],
        geneOrderList.append (aLine [0:len (aLine)])

# acquire second needed data

partOfCluster = {}

bHandle = open (sys.argv [2])

lines = bHandle.readlines ()

id = 0

for aLine in lines:
    #print aLine
    aLine = aLine.replace ("\n", "")
    words = aLine.split (" ")
    for aWord in words:
        #print aWord,
        if not partOfCluster.has_key (aWord):
            partOfCluster [aWord] = id
    
    id = id + 1
#print partOfCluster
# put together
output = open ('geneOrder12.txt', 'w+')

for aGene in geneOrderList:
    #print aGene,
    if partOfCluster.has_key (aGene):
        print partOfCluster [aGene],
    else:
        continue       
    print >> output, partOfCluster [aGene],

output.close()       
        #pickle.dump(partOfCluster[aGene], output)
#output.close()
        
