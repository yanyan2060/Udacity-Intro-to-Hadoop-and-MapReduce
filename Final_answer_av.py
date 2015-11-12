#!/usr/bin/env python
#mapper
import sys
import csv

reader = csv.reader(sys.stdin, delimiter = '\t')

for line in reader:
	if len(line) == 19:
		if not line[0].isdigit():
			continue
			
		node_id, title, tag_names, author_id, body, node_type, parent_id, abs_parent_id, added_at, score, = line[0:10]
        state_string, last_edited_id, last_activity_by_id, last_activity_at, active_revision_id, extra, = line[10:16]
        extra_ref_id, extra_count, marked = line[16:]

        if node_type == "question":
            print("{0}\tQuestion\t{1}".format(node_id, len(body)))

        if node_type == "answer":
            print("{0}\tAnswer\t{1}".format(parent_id, len(body)))


#!/usr/bin/python
#reducer
import sys

old_key = None
question_len = 0
answer_len = 0
answer_num = 0

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 3:
        continue

    this_key, this_type, this_value = data_mapped

    if old_key is not None and old_key != this_key:
        if answer_num > 0:
            answer_avg = answer_len / answer_num
        else:
            answer_avg = 0

        print("{0}\t{1}\t{2}".format(old_key, question_len, answer_avg))

        question_len = 0
        answer_len = 0
        answer_num = 0

    old_key = this_key

    if this_type == "Question":
        question_len = float(this_value)

    if this_type == "Answer":
        answer_len += float(this_value)
        answer_num += 1

if old_key is not None:
    answer_avg = answer_len / answer_num
    print("{0}\t{1}\t{2}".format(old_key, question_len, answer_avg))
