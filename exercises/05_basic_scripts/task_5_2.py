# -*- coding: utf-8 -*-
"""
Task 5.2

Ask the user to enter the IP network in the format: 10.1.1.0/24

Then print information about the network and mask in this format:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Check the script work on different net/mask combinations.

Hint: You can get the mask in binary format like this:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'

You can then take 8 bits of the binary mask using slices and convert them to decimal.

Restriction: All tasks must be done using the topics covered in this and previous chapters.
"""
#!/usr/bin/env python
from pprint import pprint

net = input ('Введите IP-сети в (формате: x.x.x.x/y): ')
add = net.split('/')[0]
mask = net.split('/')[-1]
oct = (net.split('/')[0]).split('.')
mask_zero = "0"*(32 - int(mask))
mask_one = "1"*(int(mask))
mask_bin = mask_one + mask_zero



#pprint(add)
#pprint(mask)
#pprint(mask_one)
#pprint(mask_zero)
#pprint(mask_bin)

print (f'''
Network:
{oct[0]:<16} {oct[1]:<16} {oct[2]:<16} {oct[3]:<16}
{int(oct[0]):08b} {int(oct[1]):08b} {int(oct[2]):08b} {int(oct[3]):08b}

Mask:
/{mask}
{int((mask_bin[0:8]),2):<16} {int((mask_bin[8:16]),2):<16} {int((mask_bin[16:24]),2):<16} {int((mask_bin[24:32]),2):<16}
{mask_bin[0:8]:<8} {mask_bin[8:16]:<8} {mask_bin[16:24]:<8} {mask_bin[24:32]:<8}
''')