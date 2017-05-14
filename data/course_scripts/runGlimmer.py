#!/usr/bin/python
import os
import commands
dir = "./"
for file in os.listdir(dir):
    if file.endswith('.fa'):
        basename = file.rstrip('.fa')
        cmd = ['tigr-glimmer long-orfs -n -t 1.15 %s.fa %s.long-orf-coords' % (basename, basename), 
               'tigr-glimmer extract -t %s.fa %s.long-orf-coords > %s.longorf' % (basename, basename, basename),
               'tigr-glimmer build-icm -r %s.icm < %s.longorf' % (basename, basename),
               'tigr-glimmer glimmer3 -o50 -g110 -t30 %s.fa %s.icm %s.glimmer' % (basename, basename, basename)]
        for c in cmd:
            print "Executing %s" % c
            print commands.getoutput(c)

        
