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