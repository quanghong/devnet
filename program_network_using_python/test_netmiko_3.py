from netmiko import ConnectHandler
from pprint import pprint
from inventory.config import inv

ObjFile = open('./program_network_using_python/inventory/netmiko_p3', 'r')
lines = ObjFile.readlines()
ObjFile.close()
pprint(lines)


# # Define the device to connect to
for device, info in inv.items():
    print(device)
    pprint(info)

    net_connect = ConnectHandler(**info)

    output = net_connect.send_command('show ip int brief')
    print(output)

    pprint(lines)
    output = net_connect.send_config_set(lines)
    print(output)

    output = net_connect.send_command('show vlan')
    print(output)

    break