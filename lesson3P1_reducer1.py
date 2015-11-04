__author__ = 'yanyan'
#!/usr/bin/env python

import sys

salesToal = 0
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) !=2:
        continue
    thisKey, thisSale = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", salesToal
        oldKey = thisKey;
        salesTotal = 0

    oldKey = thisKey
    salesToal += float(thisSale)

#the last item
if oldKey != None:
    print oldKey, "\t", salesToal
