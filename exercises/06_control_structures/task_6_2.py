# -*- coding: utf-8 -*-
"""
Task 6.2

Prompt the user to enter an IP address in the format 10.0.1.1
Depending on the type of address (described below), print to the stdout:
    'unicast' - if the first byte is in the range 1-223
    'multicast' - if the first byte is in the range 224-239
    'local broadcast' - if the IP address is 255.255.255.255
    'unassigned' - if the IP address is 0.0.0.0
    'unused' - in all other cases

Restriction: All tasks must be done using the topics covered in this and previous chapters.
"""
ip_add = input ('Введите IP адрес в формате 10.1.1.1: ' )
ip_oct = (ip_add.split('.'))[0]

#print(ip_add)
#print(ip_oct)

if ip_add == '255.255.255.255':
        print('local broadcast')

elif ip_add == '0.0.0.0':
        print('unassigned')
else:
    if int(ip_oct) >=240:
        print('unused')
    elif int(ip_oct) >= 224:
        print('multicast')
    elif int(ip_oct) >= 1:
        print('unicast')

