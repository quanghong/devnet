# CWS setup
<!-- username not in sudoers file -->
cat /etc/sudoers
expert ALL=(ALL) ALL

<!-- apt -->
> cat /etc/apt/apt.conf
Acquire::http::proxy "http://PROXY";
Acquire::https::proxy "http://PROXY";

<!-- git -->
git config --global http.proxy http://PROXY
git config --global https.proxy http://PROXY

<!-- docker -->
> curl -fsSL https://download.docker.com/linux/ubuntu/gpg --proxy "http://PROXY" | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

Step 4: Set Up Stable Docker Repository
> echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

<!-- terraform -->
> curl -fsSL https://apt.releases.hashicorp.com/gpg --proxy "http://PROXY" | sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg

> echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com \
  $(lsb_release -cs) main" | \
  sudo tee /etc/apt/sources.list.d/apt_releases_hashicorp_com.list > /dev/null

<!-- netplan -->
/etc/netplan/00-cws-dhcp-config.yaml
network:
    version: 2
    renderer: networkd
    ethernets:
        ens160:
            dhcp4: true
            addresses:
                - 192.168.116.128/24
            nameservers:
                addresses: [192.168.116.1]
                search: [192.168.116.1]
            routes:
                - to: default
                  via: 192.168.116.1
        ens32:
            addresses:
                - 192.168.20.100/24
            # routes:
            #     - to: default
            #       via: 192.168.20.254