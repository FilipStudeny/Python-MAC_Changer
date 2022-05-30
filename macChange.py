###############################
#         MAC CHANGER         #
###############################

import subprocess as ps
import optparse as parse
import re 

def Display_Settings(interface, mac):
    print("###############################\n"+
          "#         MAC CHANGER         #\n"+
          "###############################\n")
    
    print("[+] SETTINGS [+]")
    print("Selected Interface = " + interface)
    print("New MAC = " + mac + "\n\n")
    
    print("[+]Current MAC adress for " + interface + " [+]")
    print(interface + " : " + str(Get_Current_MAC(values.interface)))

def Change_MAC(interface, mac):
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
        
    if not values.new_mac:
        parser.error("[X] Please specify new MAC address, use --help for more info [X]")
        
    return values

def Get_Current_MAC(interface):
    ifConfigResult = ps.check_output(['ifconfig', interface])
    macResult = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifConfigResult))

    if macResult:
        return macResult.group(0)
    else:
        return "[X] ERROR: Couldn't read MAC adress [X]"


values = Get_Values()
Display_Settings(values.interface, values.new_mac)
Change_MAC(values.interface,values.new_mac)

currentMAC = Get_Current_MAC(values.interface)
if currentMAC == values.new_mac:
    print("[+] MAC adress for " + values.interface + " changed to " + values.new_mac + " [+]")
else:
    print("[X] ERROR MAC adress couldn't be changed")

