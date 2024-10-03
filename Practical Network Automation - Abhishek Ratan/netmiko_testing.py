from netmiko import ConnectHandler 

USERNAME = 'cisco'
PASSWORD = 'cisco'

list_ip = ['192.168.20.1', '192.168.20.2', '192.168.20.3', '192.168.20.4']
# ip_address = '192.168.20.1'

def test_netmiko(ip_address):
    device = ConnectHandler(device_type='cisco_ios', ip=ip_address, username=USERNAME, password=PASSWORD)
    
    output = device.send_command("show version | in uptime")
    print(output)

    output = device.send_command("show run interface gi 0/0")
    print(output)
    

    # output = device.send_command("show running-config interface fastEthernet 0/0")
    # print (output)
    # configcmds=["interface fastEthernet 0/0", "description my test"]
    # device.send_config_set(configcmds)
    # print ("After config push")
    
    
    device.disconnect()


for ip_address in list_ip: test_netmiko(ip_address)
