https://stackoverflow.com/questions/75254685/gpg-error-https-apt-releases-hashicorp-com-bionic-inrelease-the-following-si


curl -fsSL https://apt.releases.hashicorp.com/gpg | gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg

# Verify the key's fingerprint
gpg --no-default-keyring --keyring /usr/share/keyrings/hashicorp-archive-keyring.gpg --fingerprint

# The fingerprint must match 798A EC65 4E5C 1542 8C8E 42EE AA16 FCBC A621 E701, which can also be verified at https://www.hashicorp.com/security under "Linux Package Checksum Verification".

# Add the HashiCorp repo
echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list

# apt update successfully
sudo apt update