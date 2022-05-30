###############################
#         MAC CHANGER         #
###############################

import subprocess as ps
import optparse as parse
import re 

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
    (values, arguments) = parser.parse_args()
    
    if not values.interface:
        parser.error("[X] Please specify interface, use --help for more info [X]")
    elif not values.new_mac:
        parser.error("[-] Generating random MAC adress [-]")
    return values
        

values = Get_Values()
Change_MAC(values.interface,values.new_mac)

ifConfigResult = ps.check_output(['ifconfig', values.interface])

