#!/usr/bin/env python

from ciscoconfparse import CiscoConfParse

cisco_cfg = CiscoConfParse("cisco.txt")

#print cisco_cfg

crypto_maps = cisco_cfg.find_objects(r"^crypto map CRYPTO")

for crypto_map in crypto_maps:
	print
	print crypto_map.text
	for child in crypto_map.children:
		print child.text
print
