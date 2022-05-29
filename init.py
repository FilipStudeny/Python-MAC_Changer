###############################
#         MAC CHANGER         #
###############################
#!/usr/bin/python3

import subprocess as ps
import optparse as parse

def Change_MAC(interface, mac):
    print("[+] SETTINGS [+]")
    print("     Interface > " + interface)
    print("     MAC > " + mac + "\n\n")

    print("[+] Changing MAC adress for " + interface + " [+]")
    ps.call(["ifconfig", interface, "down"])
    ps.call(["ifconfig", interface, "hw ether", mac])
    ps.call(["ifconfig", interface, "up"])

    print("[+] MAC address changed [+]")

def Get_Values():
    # CLI
    parser = parse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC adress")
    return parser.parse_args()

(values, arguments) = Get_Values()
Change_MAC(values.interface,values.new_mac)

