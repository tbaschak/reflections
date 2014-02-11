# Reflections #

Various reflected attacks used in DDoS. Simple proof of concepts for lab demos.

## Requirements ##

*	Python
*	Scapy

## dns.py ##

Uses spoofed packets to request large responses from a recursive/cacheing DNS server.

## ntp.py ##

Uses spoofed packets to request monlist from affected NTP servers.

*	Uses payload from https://github.com/sensepost/ntp_monlist
