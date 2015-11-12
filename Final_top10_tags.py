#!/usr/bin/env python

#mapper

import sys
import csv

N = 10
reader = csv.reader(sys.stdin, delimiter='\t')
tags = {}

for line in reader:
    if len(line) == 19:
        if not line[0].isdigit():  # skip header
            continue

        node_id, title, tag_names, author_id, body, node_type, parent_id, abs_parent_id, added_at, score, = line[0:10]
        state_string, last_edited_id, last_activity_by_id, last_activity_at, active_revision_id, extra, = line[10:16]
        extra_ref_id, extra_count, marked = line[16:]

        if node_type == "question":
            for tag in tag_names.strip().split(" "):
                if tag in tags:
                    tags[tag] += 1
                else:
                    tags[tag] = 1

tags = sorted(tags.items(), key=lambda x: x[1], reverse=True)[0:N]

for t in tags:
    print('{0}\t{1}'.format(t[0], t[1]))
    

#!/usr/bin/env python

#reducer

import sys

N = 10
tags = {}

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    tag, occurrences = data_mapped

    if tag in tags:
        tags[tag] += int(occurrences)
    else:
        tags[tag] = int(occurrences)

tags = sorted(tags.items(), key=lambda x: x[1], reverse=True)[0:N]

for t in tags:
    print('{0}\t{1}'.format(t[0], t[1]))
