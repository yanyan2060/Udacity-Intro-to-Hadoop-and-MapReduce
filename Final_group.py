#!/usr/bin/env python
#mapper

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')

for line in reader:
    if len(line) == 19:
        if not line[0].isdigit():  # skip header
            continue

        node_id, title, tag_names, author_id, body, node_type, parent_id, abs_parent_id, added_at, score, = line[0:10]
        state_string, last_edited_id, last_activity_by_id, last_activity_at, active_revision_id, extra, = line[10:16]
        extra_ref_id, extra_count, marked = line[16:]

        if node_type == "question":
            print("{0}\t{1}".format(node_id, author_id))
        else:
            print("{0}\t{1}".format(abs_parent_id, author_id))


#!/usr/bin/env python
#reducer
import sys

old_key = None
users = []

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    this_key, this_user = data_mapped

    if old_key is not None and old_key != this_key:
        print("{0}\t{1}".format(old_key, "\t".join(users)))
        users = list()

    old_key = this_key
    users.append(this_user)

if old_key is not None:
    print("{0}\t{1}".format(old_key, "\t".join(users)))
