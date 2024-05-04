# ssh device
Unable to negotiate with 192.168.168.101 port 22: no matching key exchange method found. Their offer: diffie-hellman-group-exchange-sha1,diffie-hellman-group14-sha1,diffie-hellman-group1-sha1


Add to /etc/ssh_config
<!-- Host 192.168.168.*
   KexAlgorithms +diffie-hellman-group-exchange-sha1 -->
