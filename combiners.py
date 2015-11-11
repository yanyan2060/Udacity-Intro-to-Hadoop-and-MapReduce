#!/usr/bin/env python

#mapper

import sys
import time

week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data) == 6:
		date, hour, store, item, cost, payment = data
		day = week[time.strptime(data, "%Y-%m-%d").tm_wday]
		
		print "{0}\t{1}".format(day, cost)
		
		

#reducer

import sys

saleTotal = 0
oldKey = None

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped != 2):
		continue
	
	thisKey, thisValue = data_mapped
	
	if oldKey and oldKey != thisKey:
		print "{0}\t{1}".format(oldKey, saleTotal)
		saleTotal = 0
	oldKey = thisKey
	saleTotal += float(thisValue)
	
if oldKey:
	print "{0}\t{1}".format(oldKey, saleTotal)
	
