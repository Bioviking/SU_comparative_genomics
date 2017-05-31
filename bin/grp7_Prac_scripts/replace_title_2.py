import sys
import glob
import re
import string
filelist = []
for name in glob.glob('k_out_Cluster_*'):
    file = open(name, 'r')
    file = file.read()
    for char in file:
        file = file.replace('./', '')
        file = file.replace('.fa.txt_', ' ')
    with open('out' + name, 'w+') as outfile:
        outfile.write(file)        


