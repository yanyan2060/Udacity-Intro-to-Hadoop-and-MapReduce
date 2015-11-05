__author__ = 'yanyan'
#!/usr/bin/env python
import sys
count = 0
oldKey = None
mostpop_path = ''
mostpop_count = 0

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    thisKey, thiscount = data_mapped

    if oldKey and oldKey != thisKey:
        if count > mostpop_count:
            mostpop_count = count
            mostpop_path = oldKey

        oldKey = thisKey;
        count= 0

    oldKey = thisKey
    count += int(thiscount)
if count > mostpop_count:
    mostpop_path = oldKey
    mostpop_count = count
if mostpop_path != None:
    print mostpop_path, "\t", mostpop_count
