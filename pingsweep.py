#!/usr/bin/python3

import ipaddress
import subprocess

while True:
    network = input(
            "Which ip range would you like to ping?\n"
            "Type a single address, or use CIDR notation, like 1.2.3.0/24).\n"
    )
    try: 
        network = ipaddress.ip_network(network)
    except ValueError:
        print("\nInvalid format, please try again\n")
    else:
        break

print("\nNumber of addresses to check: " + str(network.num_addresses))
input("Press ENTER key to continue...")

hosts_alive = []
for host in network.hosts():
    p = subprocess.run(["ping", "-c", "1", "-w", "1", str(host)], stdout=subprocess.DEVNULL)  
    # one ping only
    if p.returncode == 0:
        hosts_alive.append(host)

print("\n\nHosts alive:")
if len(hosts_alive) > 0:
    print(*hosts_alive, sep="\n")
else:
    print("None")
