#!/usr/bin/env python

import yaml
import json

my_list = range(5)
my_list.append('Python Programming')
my_list.append('Is Fun')
my_list.append({})
my_list[-1]['IP_ADDR'] = '10.10.10.239'
my_list[-1]['HOSTNAME'] = 'testbox'
my_list[-1]['DOMAIN_NAME'] = 'someplace.net'

with open("Lesson1Number6_create_first_yaml.yml", "w") as filehandle1:
	filehandle1.write(yaml.dump(my_list, default_flow_style=False))
	filehandle1.close()

with open("Lesson1Number6_create_first_json.json", "w") as filehandle2:
	json.dump(my_list, filehandle2)
	filehandle2.close()

