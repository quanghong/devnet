import subprocess

list_ip = ['192.168.20.1', '192.168.20.2', '192.168.20.3', '192.168.20.4', '192.168.20.254']

for ip in list_ip:
    data =  subprocess.Popen("ping " + ip + " -w 1",  shell=True, stdout=subprocess.PIPE).stdout
    data =  data.read().decode()
    print(data)



