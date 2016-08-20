#!/usr/bin/env python


# Should create a For Each loop using a tuple or dictionary

from snmp_helper import snmp_get_oid,snmp_extract

COMMUNITY_STRING = 'galileo'
SNMP_PORT = 161
IP = '184.105.247.70'
OID = '1.3.6.1.2.1.1.5.0'

snmp_device = (IP, COMMUNITY_STRING, SNMP_PORT)

snmp_data = snmp_get_oid(snmp_device, oid=OID)
#print snmp_data

output = snmp_extract(snmp_data)

print '\n\n'
print output
print '\n\n'

OID = '1.3.6.1.2.1.1.1.0'
snmp_data = snmp_get_oid(snmp_device, oid=OID)
#print snmp_data

output = snmp_extract(snmp_data)

print output
print '\n\n'

IP = '184.105.247.71'
OID = '1.3.6.1.2.1.1.5.0'
snmp_device = (IP, COMMUNITY_STRING, SNMP_PORT)
snmp_data = snmp_get_oid(snmp_device, oid=OID)

output = snmp_extract(snmp_data)

print output
print '\n\n'

OID = '1.3.6.1.2.1.1.1.0'
snmp_data = snmp_get_oid(snmp_device, oid=OID)
#print snmp_data

output = snmp_extract(snmp_data)

print output
print '\n\n'
