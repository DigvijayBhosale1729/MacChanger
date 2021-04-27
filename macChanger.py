# We'll be using the subprocess.call function and ifconfig
# Reason is - the call function waits for command to be executed before going ahead with the program
import subprocess
import optparse
import re


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option('-i', '--interface', dest='interface', help='Interface that needs a MAC Address Change')
    parser.add_option('-m', '--mac', dest='new_mac', help='The New MAC Address that we want')
    (options, arguments) = parser.parse_args()
    return options


def change_mac(interface, mac_addr):
    # I'm putting a comma in the subprocess.call() instead of concatenating the string, to prevent code injection.
    # When i do that, the program knows that the command is ifconfig
    # And the rest of the things are parameters
    try:
        subprocess.call("ifconfig "+ interface + " down", shell=True)
        print("[+] Interface Down")
    except:
        print("[-] Error in disabling interface. Make sure you are logged in as root.")


    try:
        subprocess.call("ifconfig "+ interface + " hw ether "+ mac_addr, shell=True)
        print("[+] MAC Address Changed")
    except:
        print("[-] Error in Changing MAC. Make sure you are logged in as root.")

    try:
        subprocess.call("ifconfig "+ interface+ " up", shell=True)
        print("[+] Interface is back Up")
    except:
        print("[-] Error in Enabling interface. Make sure you are logged in as root.")


def get_current_mac(interface):
    ifc_results = str(subprocess.check_output(['ifconfig', interface]))
    # To find out the MAC Address from the output, we use regex
    # to fing the MAC Address, the regex is
    # \w\w:\w\w:\w\w:\w\w:\w\w:\w\w
    # the meaning of this is --> \w is any alphanumeric char
    # and the : is the : itself
    curr_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifc_results)
    # this is the regex format
    # curr_mac is a group and we want the first element

    if curr_mac:
        print("[+] Current MAC Address is ", curr_mac.group(0))
        return curr_mac.group(0)
    else:
        print("[-] MAC Address not found for selected Interface")


options = get_arguments()
current_mac = get_current_mac(options.interface)
change_mac(options.interface, options.new_mac)
current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("[+] MAC Address changed Successfully ")
else:
    print("[-] Could not change current MAC, some error occurred")

