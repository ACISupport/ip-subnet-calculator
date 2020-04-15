#! /usr/bin/env python
"""
This script is a part of a tutorial to build a Python subnet Calculator.

The script accepts string inputs in the following formats:
`192.168.1.0/24` or `192.168.2.0/255.255.255.0`

Example Usage:

    $ python subnet_calc.py 192.168.1.0/26

Output:
    IP Subnet Calculator
    Subnet: 192.168.0.0/24

    Network:   192.168.0.0/24 (Private Internet)
    Netmask:   255.255.255.0 = 24
    Wildcard:  0.0.0.255

    Broadcast: 192.168.0.255
    HostMin:   192.168.0.1
    HostMax:   192.168.0.254
    Hosts/Net: 254
"""
import ipaddress


def main():
    """
    Execution of the script starts here
    """

    # Uncomment the line below the print() welcome message
    print("IP Subnet Calculator")

    # create a network variable
    network = '192.168.0.0/24'

    network_object = ipaddress.ip_network(network)

    # Wildcard
    netmask = str(network_object.netmask)
    netmask_octets = netmask.split('.')

    wilcard_octets = []
    for octet in netmask_octets:
        wildcard = str(255 - int(octet))
        wilcard_octets.append(wildcard)

    dot = '.'
    wildcard = dot.join(wilcard_octets)

    hosts = list(network_object.hosts())
    hostcount = len(hosts)

    print(f"Network:  {network_object} (Private Internet)")
    print(f"Netmask:   {network_object.netmask} =  {network_object.prefixlen})")
    print(f"Wildcard: {wildcard}")
    # print(Broadcast: 192.168.0.255)
    # print(HostMin:   192.168.0.1)
    # print(HostMax:   192.168.0.254)
    # print(Hosts/Net: 254)




if __name__ == "__main__":
    main()
