import snmp_helper

if True:
	IP1 = '184.105.247.70'
	IP2 = '184.105.247.71'
	user_name = 'pysnmp'
	auth_key = 'galileo1'
	encrypt_key = 'galileo1'
	snmp_user = (user_name, auth_key, encrypt_key) #creates a tuple
	pynet_rtr1 = (IP1, 161) #IP and SNMP port, uses standard port 161
	pynet_rtr2 = (IP2, 161)

snmp_data = snmp_helper.snmp_get_oid_v3(pynet_rtr2, snmp_user, oid='1.3.6.1.2.1.1.5.0')
output = snmp_helper.snmp_extract(snmp_data)
print output

