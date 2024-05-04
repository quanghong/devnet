from netmiko import ConnectHandler
from pprint import pprint
from inventory.config import inv

ObjFile = open('./tasks/inventory/sw-config', 'r')
lines = ObjFile.readlines()
ObjFile.close()
pprint(lines)


# # Define the device to connect to
for device, info in inv.items():
    print(device)
    pprint(info)

    net_connect = ConnectHandler(**info)
    # net_connect.find_prompt()
    output = net_connect.send_command('show ip int brief')
    print(output)


# # config_commands = ['int loop 0', 'ip address 1.1.1.1 255.255.255.0']
# # output = net_connect.send_config_set(config_commands)
# # print(output)

# output = net_connect.send_command('show vlan')
# print(output)

# # for n in range (21,22):
# #     print("Creating VLAN " + str(n))
# #     config_commands = ['vlan ' + str(n), 'name Python_VLAN ' + str(n)]
# #     output = net_connect.send_config_set(config_commands)
# #     print(output)