#!/usr/bin/env python
import sys
import csv

#mapper

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

for line in sys.stdin:
	if len(line) == 5:
		if str(line[0].isdigit()):
			writer.writerow([int(line[0])] + ['A'] + [line[1:]])
			
 if len(line) == 19:
        # forum_node.tsv
        if str(line[0]).isdigit():  # don't print header
            writer.writerow([int(line[3])] + ['B'] + line[0:3] + line[5:10])
			

#reducer

import sys
import csv

olduid = None
curuser = None
entries = []

reader = csv.reader(sys.stdin, delimiter = '\t')

for line in reader:
	if len(line) == 10:
        uid, _, pid, title, tag_names, node_type, parent_id, abs_parent_id, added_at, score = line
    elif len(line) == 6:
        uid, _, reputation, gold, silver, bronze = line
        curr_user = {'uid': uid, 'reputation': reputation, 'gold': gold, 'silver': silver, 'bronze': bronze}
    else:
        continue
		
	 if old_uid is not None and uid != old_uid:
        # print pending entries
        for entry in entries:
            if curr_user is not None:
                print('\t'.join([entry['pid'], entry['title'], entry['tag_names'], curr_user['uid'], entry['node_type'],
                                 entry['parent_id'], entry['abs_parent_id'], entry['added_at'], entry['score'],
                                 curr_user['reputation'], curr_user['gold'], curr_user['silver'], curr_user['bronze']]))
        curr_user = None
        entries = []

    if curr_user is not None and len(line) == 10:
      
        print('\t'.join([pid, title, tag_names, curr_user['uid'], node_type, parent_id, abs_parent_id, added_at, score,
                         curr_user['reputation'], curr_user['gold'], curr_user['silver'], curr_user['bronze']]))
    elif curr_user is None and len(line) == 10:
        
        entries.append(
            {'uid': uid, 'pid': pid, 'title': title, 'tag_names': tag_names, 'node_type': node_type,
             'parent_id': parent_id, 'abs_parent_id': abs_parent_id, 'added_at': added_at, 'score': score})

    old_uid = uid

if old_uid is not None:
    for entry in entries:
        print('\t'.join([entry['pid'], entry['title'], entry['tag_names'], curr_user['uid'], entry['node_type'],
                         entry['parent_id'], entry['abs_parent_id'], entry['added_at'], entry['score'],
                         curr_user['reputation'], curr_user['gold'], curr_user['silver'], curr_user['bronze']]))

