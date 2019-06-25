#!/usr/bin/env python

import subprocess  # allows us to execute OS shell commands
import optparse  # allows us to create and specify arguments and help text


def get_arguments():
    parser = optparse.OptionParser()  # create instance of object parser
    parser.add_option("-i", "--interface", dest="interface", help="Interface whose MAC address you want to change")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options, arguments) = parser.parse_args()  # so parser can read and understand the supplied arguments
    if not options.interface:  # if no interface is specified
        parser.error("[-] Please specify an interface. Use --help for more info.")
    elif not options.new_mac:  # if no MAC address is specified
        parser.error("[-] Please specify a new MAC address. Use --help for more info.")
    return options  # return options so they can be accessed from global scope


def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac + "\n")  # displays values of variables
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])
    subprocess.call(["ifconfig", interface])  # so I don't have to keep typing it every time to check it worked!


user_input = get_arguments()  # get user supplied interface and new MAC address from get_arguments function call
change_mac(user_input.interface, user_input.new_mac)
