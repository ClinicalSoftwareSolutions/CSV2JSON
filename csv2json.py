#!/usr/bin/python

import argparse
import sys
import csv
import json

parser = argparse.ArgumentParser(description='Convert an excel CSV file to JSON')
parser.add_argument('csvfile', help="The CSV to parse (required)")
parser.add_argument('-f', '--fieldnames', help="Field names for the data", nargs='+', dest='fieldnames')

args = parser.parse_args()

with open( args.csvfile, 'r' ) as f:
  reader = csv.DictReader( f, fieldnames = ( args.fieldnames ) )
  print json.dumps( [ row for row in reader ], indent=3 )
