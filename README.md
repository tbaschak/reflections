# Reflections #

Various reflected attacks used in DDoS. Simple proof of concepts for lab demos.

## Requirements ##

*	Python
*	Scapy

## dns.py ##

Uses spoofed packets to request large responses from a recursive/cacheing DNS server.

## ntp.py ##

Uses spoofed packets to request monlist from affected NTP servers.

## snmp.py ##

Uses spoofed packets to make large snmpbulk requests from a server.

*	Uses logic from http://www.prolexic.com/kcresources/white-paper/white-paper-snmp-ntp-chargen-reflection-attacks-drdos/analysis-of-drdos-dns-reflection-white-paper_i.html
*	Uses improved request from http://www.nothink.org/misc/snmp_reflected.php

## Disclaimer ##

This information is provided to assist network administrators in defending their own networks. It is not intended to assist with DoSing remote sites or exploiting services on those sites, or for imformation gathering purposes beyond those allowed by law. I hereby disclaim any responsibility for actions taken based upon the code in this package, and urge all who seek information towards a destructive end to reconsider their life, and do something constructive instead.

Obviously these tools can be disruptive if not used in a lab environment. My arguement for having them public is, if the bad guys are already doing this, they already know how. We all need to be able to test equipment under these types of load, this code is a place to start testing them under.

