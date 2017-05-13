#!/usr/bin/python
# This script serves only as an example.
# Access to it, does not imply that you must use it.
# Whether it delivers output you want is up to you to decide, or modify it.

import argparse
import sys
from Bio.Blast import NCBIXML

class BlastParser:
    def __init__(self, xmlfile):
        self.xmlit = NCBIXML.parse(xmlfile)

    def __iter__(self):
        return self

    def next(self):
        dict = {}
        try:
            # For each query get record
            record = self.xmlit.next()
            # Get number of alignments found for current query
            alignments_len = len(record.alignments)
            if alignments_len > 0:
                # Found hits for this query
                hitList = []
                # Iterate all hits
                for hits in record.alignments:
                    # Iterate all hsps for current hit
                    # and sum up score for local alignment regions
                    score = 0 # This variable contains total score for all matching regions between query and target
                    for hsp in hits.hsps:
                        # Sum score from every hsp
                        score += hsp.bits
                    # Save hit id and hit score in tuple
                    hitTuple = (str(hits.hit_def), score)
                    # Add tuple to list
                    hitList.append(hitTuple)
                # Add list of tuples (hitid,score) hits
                # to dictionary with key as query
                dict[str(record.query)] = hitList
        except StopIteration:
            raise
        return dict
#=============================================================================================
parser = argparse.ArgumentParser()
parser.add_argument('xmlfile', nargs='?', type=argparse.FileType('r'),
                    default=sys.stdin)
args = parser.parse_args()

bparser = BlastParser(args.xmlfile)
# Iterate queries
for result in bparser:
    # Display dictionary
    # Key is query sequence
    # Value is a list of pairs Target,Score

    # print result

    # Now you need to get highest scoring sequence for each genome
    # You can run this script per genome and identify highest scoring sequence
    # Or combine all genomes, and modify this script such that it finds best scoring target sequence one per genome

    # Example
    # Iterate all scores and sequences matching current query
    for key, values in result.iteritems():
        # Iterate all values
        largestscore = 0
        bestsequence = ''
        for value in values:
            target, score = value
            # print "Found target %s with score %d" % value
            if score > largestscore:
                largestscore = score
                bestsequence = target
        print "Found highest scoring sequence %s with score %d" % (bestsequence, largestscore)

# For documentation on XML format
# http://biopython.org/DIST/docs/tutorial/Tutorial.html#htoc92
