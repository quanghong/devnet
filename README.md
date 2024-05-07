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