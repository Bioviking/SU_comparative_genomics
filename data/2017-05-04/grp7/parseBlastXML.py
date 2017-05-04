#!/usr/bin/python
import argparse
import sys
from Bio.Blast import NCBIXML

parser = argparse.ArgumentParser()
parser.add_argument('infile', nargs='?', type=argparse.FileType('r'),
                    default=sys.stdin)
parser.add_argument('outfile', nargs='?', type=argparse.FileType('w'),
                    default=sys.stdout)
args = parser.parse_args()

for blastRecord in NCBIXML.parse(args.infile):
    for blastAlignment in blastRecord.alignments:
        title = "%s_%s" % (blastRecord.database, blastAlignment.hit_def)
        sequence = str(blastAlignment.hsps[0].sbjct)
        output = "> %s\n%s\n" % (title, sequence.replace('-', ''))
        args.outfile.write(output)
        break
