# devnet
Learning DevNet Certifications

# CWS setup
<!-- username not in sudoers file -->
cat /etc/sudoers
expert ALL=(ALL) ALL

<!-- apt -->
> cat /etc/apt/apt.conf
Acquire::http::proxy "http://proxy.hcm.fpt.vn:80/";
Acquire::https::proxy "http://proxy.hcm.fpt.vn:80/";

<!-- git -->
git config --global http.proxy http://proxy.hcm.fpt.vn:80
git config --global https.proxy http://proxy.hcm.fpt.vn:80

<!--  -->
> curl -fsSL https://download.docker.com/linux/ubuntu/gpg --proxy "http://proxy.hcm.fpt.vn:80" | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

Step 4: Set Up Stable Docker Repository
> echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null


# GPG is required for the package signing key
sudo apt install gpg

# Download the signing key to a new keyring
wget -O- https://apt.releases.hashicorp.com/gpg | gpg --dearmor | sudo tee /usr/share/keyrings/hashicorp-archive-keyring.gpg

# Verify the key's fingerprint
gpg --no-default-keyring --keyring /usr/share/keyrings/hashicorp-archive-keyring.gpg --fingerprint

# The fingerprint must match 798A EC65 4E5C 1542 8C8E 42EE AA16 FCBC A621 E701, which can also be verified at https://www.hashicorp.com/security under "Linux Package Checksum Verification".

# Add the HashiCorp repo
echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list

# apt update successfully
sudo apt update