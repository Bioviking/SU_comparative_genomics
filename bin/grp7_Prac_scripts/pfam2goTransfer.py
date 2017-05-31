#!/usr/bin/python2
import sys
import re

aHandle = open (sys.argv [1])
lines = aHandle.readlines ()

pfam2go = {}

for aLine in lines:

	if not "!" in aLine:

		aLine = aLine.replace ("\n", "")
		aLine = aLine.replace ("Pfam:", "")
		words = aLine.split (" ")
		domain = words [0]
		GO = words [len (words) - 1]

		if pfam2go.has_key (domain):

			pfam2go [domain] = pfam2go [domain] + "\t" + GO

		else:

			pfam2go [domain] = GO

aHandle.close ()

aHandle = open (sys.argv [2])
lines = aHandle.readlines ()

for aLine in lines:

	aLine = aLine.replace ("\n", "")
	words = aLine.split ("\t")
	ac = words [0]
	arch = words [1]
	print arch
	lDomains = {}

	for domain in arch.split ():
                m = re.match('.*(PF[0-9A-Z]+).', domain)
                if m:
                    lDomains [m.group(1)] = ""

	lPredictions = {}

	for domain in lDomains.keys ():

		if pfam2go.has_key (domain):

			for aGO in pfam2go [domain].split ("\t"):

				lPredictions [aGO] = ""

	predictedHere = "\t".join (lPredictions.keys ())

	print ac, "->", predictedHere
	

aHandle.close ()
