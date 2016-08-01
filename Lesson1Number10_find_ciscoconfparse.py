#!/usr/bin/env python

#Lesson1Number10
from ciscoconfparse import CiscoConfParse

cisco_cfg = CiscoConfParse("cisco.txt")

print "\n\ncrypto map entries not using AES\n"

transform_list = cisco_cfg.find_objects(r"set transform-set")

results = []

for line in transform_list:
	if not line.re_search(r"AES-SHA"):
		results.append([line.parent.text, line.text])

for result in results:
	print result

