import yaml
import json

from pprint import pprint as pp
#YAML
with open("Lesson1Number6_create_first_yaml.yml") as f:
	new_list_yaml = yaml.load(f)
	f.close()

#Pretty Prints the YAML file
print "\n\nThis is YAML\n"
pp(new_list_yaml)


#JSON
with open("Lesson1Number6_modified_first_JSON.json") as g:
	new_list_json = json.load(g)
	g.close()

#Pretty Prints the JSON file
print "\n\nThis is JSON\n"
pp(new_list_json)

print "\n\n"
