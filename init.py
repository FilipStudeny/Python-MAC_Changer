###############################
#         MAC CHANGER         #
###############################
#!/usr/bin/env python3

import subprocess as ps
import optparse as parse

parser = parse.OptionParser()
parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
parser.add_option("-m", "--mac", dest="new_mac", help="New MAC adress")

parser.parse_args()

interface = input("interface = ")

print("[+] Changing MAC adress for " + interface + " [+]")
ps.call(["ifconfig", interface, "down"])
ps.call(["ifconfig", interface, "hw ether 00:11:22:33:44:55"])
ps.call(["ifconfig", interface, "up"])