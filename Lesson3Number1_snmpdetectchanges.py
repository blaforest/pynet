#!/usr/bin/env python

#from snmp_helper import snmp_get_oid,snmp_extract
import snmp_helper

COMMUNITY_STRING = 'galileo'
SNMP_PORT = 161


if True:
        IP1 = "184.105.247.70"
        IP2 = "184.105.247.71"
        user_name = 'pysnmp'
        auth_key = 'galileo1'
        encrypt_key = 'galileo1'
        snmp_user = (user_name, auth_key, encrypt_key) #creates a tuple
        pynet_rtr1 = (IP1, 161) 
        pynet_rtr2 = (IP2, 161)

snmp_oids = (
	('sysName', '1.3.6.1.2.1.1.5.0', None),
	('sysUptime', '1.3.6.1.2.1.1.3.0', None),
	('ifDescr_fa4', '1.3.6.1.2.1.2.2.1.2.5', None),
	('ifInOctets_fa4', '1.3.6.1.2.1.2.2.1.10.5', True),
	('ifInUcastPkts_fa4', '1.3.6.1.2.1.2.2.1.11.5', True),
	('ifOutOctets_fa4', '1.3.6.1.2.1.2.2.1.16.5', True),
	('ifOutUcastPkts_fa4', '1.3.6.1.2.1.2.2.1.17.5', True),
	)

for node_descr, node_oid, node_isCount in snmp_oids:
	snmp_data = snmp_helper.snmp_get_oid_v3(pynet_rtr2, snmp_user, oid=node_oid)
	output = snmp_helper.snmp_extract(snmp_data)
	print "%s %s" % (node_descr, output)

