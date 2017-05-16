import sys
import re

# acquire first needed data

geneOrderList = []
aHandle = sys.argv[1]
print(aHandle)
aHandle = open(aHandle)
print(aHandle)
lines = aHandle.readlines()

for aLine in lines:
	aLine = aLine.replace("\n", "")
	if aLine.startswith(">"):
		# print aLine [1:len (aLine)],
		geneOrderList.append(aLine[1:len(aLine)])
		
# acquire second needed data

partOfCluster = {}
bHandle = sys.argv[2]
bHandle = open(bHandle)
lines = bHandle.readlines()
_id_ = 0

for aLine in lines:
	aLine = aLine.replace("\n", "")
	words = aLine.split("\t")
	for aWord in words:
		if not partOfCluster.key(aWord):
			partOfCluster[aWord] = _id_
	_id_ = _id_ + 1

# put together

for aGene in geneOrderList:
	if partOfCluster.key(aGene):
		print(partOfCluster[aGene])
		output.write(partOfCluster[aGene])
