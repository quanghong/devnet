import os
from netmiko import ConnectHandler
from dotenv import load_dotenv

load_dotenv()
USERNAME = os.getenv('USERNAME_DEV')
PASSWORD = os.getenv('PASSWORD_DEV')
# print(USERNAME, PASSWORD)


list_ip = ['192.168.20.1', '192.168.20.2', '192.168.20.3', '192.168.20.4']
template="""logging host 192.168.20.254 transport tcp port 514
    logging trap 6
    interface loopback 30
    description "{rtr} loopback interface\""""


#step 1
#fetch the hostname of the router for the template
for ip in list_ip:
    device = ConnectHandler(device_type='cisco_ios', ip=ip, username=USERNAME, password=PASSWORD)
    output = device.send_command("show run | in hostname")
    output = output.split(" ")
    hostname = output[1]
    generatedconfig = template.replace("{rtr}", hostname)


    #step 2
    #push the generated config on router
    #create a list for generateconfig
    generatedconfig = generatedconfig.split("\n")
    print(generatedconfig)
    device.send_config_set(generatedconfig)
    
    
    # #step 3:
    #perform validations
    print("********")
    print("Performing validation for :", hostname + "\n")
    output = device.send_command("show logging")
    if ("encryption disabled, link up"):
        print("Syslog is configured and reachable")
    else:
        print("Syslog is NOT configured and NOT reachable")
    
    if ("Trap logging: level informational" in output):
        print("Logging set for informational logs")
    else:
        print("Logging not set for informational logs")
        print("\nLoopback interface status:")

    output = device.send_command("show interfaces description | in loopback interface")
    print (output)
    print ("************\n")