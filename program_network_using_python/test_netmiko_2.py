from netmiko import ConnectHandler
from pprint import pprint
from inventory.config import inv

# Define the device to connect to
sw1 = inv.get("vios-l2-sw1")
pprint(sw1)


net_connect = ConnectHandler(**sw1)
#net_connect.find_prompt()
output = net_connect.send_command('show ip int brief')
print(output)

# config_commands = ['int loop 0', 'ip address 1.1.1.1 255.255.255.0']
# output = net_connect.send_config_set(config_commands)
# print(output)

output = net_connect.send_command('show vlan')
print(output)

# for n in range (21,22):
#     print("Creating VLAN " + str(n))
#     config_commands = ['vlan ' + str(n), 'name Python_VLAN ' + str(n)]
#     output = net_connect.send_config_set(config_commands)
#     print(output)