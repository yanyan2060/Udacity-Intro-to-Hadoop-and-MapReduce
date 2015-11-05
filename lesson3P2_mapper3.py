__author__ = 'yanyan'

import sys
from urlparse import urlparse

for line in sys.stdin:
    line = line.strip()
    first = line.find("\"")
    second = line.find("\"")
    if second > first and first > 1:
        request = line[first + 1: second]
        url = request.split()[1]
        name = urlparse(url)
        print "{0}\t{1}".format(name.path, 1)
