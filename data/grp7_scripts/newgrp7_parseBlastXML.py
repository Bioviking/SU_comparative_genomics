import argparse
import sys
from Bio.Blast import Record 
from Bio.Blast import NCBIXML
result_handle = open("best_hits.XML")
'''
parser = argparse.ArgumentParser()
parser.result_handle('xmlfile', nargs='?', type=argparse.FileType('r'),
                    default=sys.stdin)
parser.add_argument('outfile', nargs='?', type=argparse.FileType('w'),
                    default=sys.stdout)
args = parser.parse_args()
'''
blast_records = NCBIXML.parse(result_handle)

parser.add_argument('outfile', nargs='?', type=argparse.FileType('w'),
                    default=sys.stdout)
args = parser.parse_args()

for blast_record in blast_records:
    for alignment in blast_record.alignments:
        title = "%s_%s" % (blastRecord.database, blastAlignment.hit_def)
        sequence = str(blastAlignment.hsps[0].sbjct)
        output = "> %s\n%s\n" % (title, sequence.replace('-', ''))
        args.outfile.write(output)
        break



            
'''
parse(handle, debug=0)
	source code 

Returns an iterator a Blast record for each query.

Incremental parser, this is an iterator that returns Blast records. It uses the BlastParser internally.

handle - file handle to and XML file to parse debug - integer, amount of debug information to print

This is a generator function that returns multiple Blast records objects - one for each query sequence given to blast. The file is read incrementally, returning complete records as they are read in.

Should cope with new BLAST 2.2.14+ which gives a single XML file for multiple query records.

Should also cope with XML output from older versions BLAST which gave multiple XML files concatenated together (giving a single file which strictly speaking wasn't valid XML).
'''
