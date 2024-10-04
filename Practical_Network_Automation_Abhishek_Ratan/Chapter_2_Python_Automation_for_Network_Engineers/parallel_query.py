from netmiko import ConnectHandler
from datetime import datetime
from threading import Thread
from dotenv import load_dotenv
from pysnmp.hlapi import *
import os

load_dotenv()
USERNAME = os.getenv('USERNAME_DEV')
PASSWORD = os.getenv('PASSWORD_DEV')
# print(USERNAME, PASSWORD)

list_ip = ['192.168.20.1', '192.168.20.2', '192.168.20.3', '192.168.20.4']
startTime = datetime.now()

threads = []
def checkparallel(ip):
     device = ConnectHandler(device_type='cisco_ios', ip=ip, username=USERNAME, password=PASSWORD)
     output = device.send_command("show run | in hostname")
     output = output.split(" ")
     hostname = output[1]
     print ("\nHostname for IP %s is %s" % (ip,hostname))
    
for ip in list_ip:
 t = Thread(target=checkparallel, args= (ip,))
 t.start()
 threads.append(t)

#wait for all threads to completed
for t in threads:
    t.join()


print ("\nTotal execution time:")
print(datetime.now() - startTime)