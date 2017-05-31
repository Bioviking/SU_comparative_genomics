#!/usr/bin/python
import re
import sys

with open(sys.argv[1], 'r') as uniprot:
    for line in uniprot:
        m = re.match('>.*GN=([A-Z0-9]+)', line)
        if m:
            genename = m.group(1)
            print genename
