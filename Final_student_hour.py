#!/usr/bin/env python

#mapper

import sys
import csv
from dateutil.parser import parser

reader = csv.reader(sys.stdin, delimiter = '\t')

for line in reader:
	if len(line) == 19:
		if not line[0].isdigit(): #first header line
			continue
		
		author_id = line[3]
		added_at = parse(line[8])
		
		print "{0}\t{1}".format(author_id, added_at)
		
		
#!/usr/bin/env python

#reducer

import sys

oldKey = None
hour = [0 for i in range (24)]

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped) != 2:
		continue
		
	thisKey, thisHour = data_mapped
	
	if oldKey and oldKey != thisKey:
		maxhour = max(hour)
		
		for i, j in enumerate(hour):
			if j == maxhour:
				print "{0}\t{1}".format(oldKey, i)
				
		hour = [0 for i in range (24)]
		
	oldKey = thisKey
	hour[int(thisHour)] += 1
	
if oldKey:
	maxhour = max(hour)
	for i, j in enumerate(hour):
		if j == maxhour:
			print "{0}\t{1}".format(oldKey, i)
