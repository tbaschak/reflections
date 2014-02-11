# Reflections NTP monlist Lab Setup #

To set up an effect NTP monlist lab, you will need the following:

*	CLOSED network
*	NTP server with ~500 or so NTP clients. Packets from fake clients can be preloaded to generate large monlist responses.
	*	Should make a script to preload an NTP server with random requests from random client IPs
*	Attacker on a 100mbps port (smaller port than reflector or victim)
*	Reflector on a 1000mbps port
*	Victim on a 1000mbps port (to measure traffic as accurately as possible)

