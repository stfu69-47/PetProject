#!/usr/bin/env python3

# from sys import argv

interface = input("Enter your favorite interface: ")
vlan = input("Enter your favorite vlan port: ")

access_template = ['switchport mode access',
                    'switchport access vlan {}',
                    'switchport nonegotiate',
                    'spanning-tree portfast',
                    'spanning-tree bpduguard enable']

print('\n' + '-' * 50)
print('interface {}'.format(interface))
print('\n'.join(access_template).format(vlan))
