# ssh -o KexAlgorithms=diffie-hellman-group1-sha1 test@123.123.123.123

# Copy this file to config.py, and update config.py with real inventory data
inv = {
    "vios-l2-sw1": {
        "device_type": "cisco_ios",
        "host": "192.168.168.101",
        # "port": 22,
        "username": "cisco",
        "password": "cisco"
    },
    "vios-l2-sw2": {
        "device_type": "cisco_ios",
        "host": "192.168.168.102",
        # "port": 22,
        "username": "cisco",
        "password": "cisco"
    },
    "vios-l2-sw3": {
        "device_type": "cisco_ios",
        "host": "192.168.168.103",
        # "port": 22,
        "username": "cisco",
        "password": "cisco"
    },
    "vios-l2-sw4": {
        "device_type": "cisco_ios",
        "host": "192.168.168.104",
        # "port": 22,
        "username": "cisco",
        "password": "cisco"
    },
    "vios-l2-sw5": {
        "device_type": "cisco_ios",
        "host": "192.168.168.105",
        # "port": 22,
        "username": "cisco",
        "password": "cisco"
    }
}
