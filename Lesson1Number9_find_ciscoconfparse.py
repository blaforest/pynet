#!/usr/bin/env python

#Lesson1Number9 trying a different way
from ciscoconfparse import CiscoConfParse

cisco_cfg = CiscoConfParse("cisco.txt")

print "\n\ncrypto map entries using PFS group2\n"
crypto_maps = cisco_cfg.find_objects_w_child(parentspec=r"^crypto map CRYPTO", childspec=r"set pfs group2")

for crypto_map in crypto_maps:
	print crypto_map.text
