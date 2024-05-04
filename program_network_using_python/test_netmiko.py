from netmiko import ConnectHandler
from pprint import pprint

"""
Netmiko is a fork of Paramiko and simplifies the
channel management when connecting to a network device

Example from "Mastering Python Networking" by Eric Chou
"""

from inventory.config import inv

# Define the device to connect to
sw1 = inv.get("vios-l2-sw1")
pprint(sw1)

# Connect to the device
net_connect = ConnectHandler(**sw1)

# Automatically knows the prompt
net_connect.find_prompt()  # "iosv-1#"

# Run show version
output = net_connect.send_command("show version")
print(output)

# Send multiple commands at once
# output2 = net_connect.send_config_set(["logging buffered 19999", "logging host 10.1.1.1"])