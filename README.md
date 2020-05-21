# Readme
---------------

## python decorator pratice

````
@decorator
def func(*args, **kwargs):
    ...

equivlant to
def func(*args, **kwargs):
    ...
func = decorator(func)    
````

## First commit via GIT hub

### Second commit via Git hub

- section one 
- section two 
* paragraph one
* paragraph **two**
add new map/lambda/yield test

vlc https://iptv-org.github.io/iptv/index.m3u


basecamp@basecamp07:~$ pivpn add
Enter a Name for the Client: wei
::: Client Keys generated
::: Client config generated
::: Updated server config
::: WireGuard restarted
======================================================================
::: Done! wei.conf successfully created!
::: wei.conf was copied to /home/basecamp/configs for easy transfer.
::: Please use this profile only on one device and create additional
::: profiles for other devices. You can also use pivpn -qr
::: to generate a QR Code you can scan with the mobile app.
======================================================================



Requirements
-  Firewall open dst-nat to WireGuard server on UDP port 51820 (Mikortik)
-  WireGuard Server (10.67.19.200) - no lxc or vm machine.
-  WireGuard Client (ubuntu) - no lxc or vm machine

Document references:
* https://github.com/pivpn/pivpn (server installation)
* https://www.wireguard.com/install/#ubuntu-1904-module-tools (client installation)
* https://wiki.archlinux.org/index.php/WireGuard (concept and details, specailly on point-to-site routing paragraph)
* https://linuxize.com/post/how-to-set-up-wireguard-vpn-on-ubuntu-18-04/ (general tutorial)
* raspberry https://engineerworkshop.com/blog/how-to-set-up-wireguard-on-a-raspberry-pi/#set-up-the-wireguard-client 
* raspberry client: https://engineerworkshop.com/blog/how-to-set-up-a-wireguard-client-on-linux-with-conf-file/ 
------------------------
if troubles on raspberry client installation, check the following and install kernel-headers
find /lib/modules -name wireguard.ko
dpkg -s wireguard-tools
dpkg -s wireguard-dkms
dpkg -s raspberrypi-kernel
dpkg -s raspberrypi-kernel-headers
dkms status
------------------------

Installation:
- Server
    interactive way, and following instruction
    - curl -L https://install.pivpn.io | bash
    - pivpn -a -n <client>
    - pivpn list 
    - pivpn remove
    copy from ˜/configs/<*>.conf to each client
    autostart
    $ sudo systemctl enable wg-quick@wg0.service
    $ sudo systemctl daemon-reload 
    $ sudo systemctl start wg-quick@wg0
    $ systemctl status wg-quick@wg0

    to remove service
    $sudo systemctl stop wg-quick@wg0
    $sudo systemctl disable wg-quick@wg0.service
    $sudo rm -i /etc/systemd/system/wg-quick@wg0*
    $sudo systemctl daemon-reload
    $sudo systemctl reset-failed


- Client
    - apt install resolvconf
    - mkdir -p /etc/wireguard
    - chown root:root /etc/wireguard
    - chmod 700 /etc/wireguard
    - cp <client>.conf /etc/wireguard/
    - wg-quick up <client>
    automatic restart :
    $ sudo systemctl enable wg-quick@<client>.service
    $ sudo systemctl daemon-reload
    $ sudo systemctl status wg-quick@wg0


- Mikrotik configuration
    IP/Firewall/NAT
    General
    - Chain: dstnat
    - Dst.Address : <ip public>
    - Protocol 17(udp)
    - Dst Port: 51820
    Action
    - Action: dst-nat
    - To Addresses: 10.67.19.200
    - To Ports: 51820

    Access to server via tunnel wireguard vpn
    ssh basecamp@10.6.0.1 <wireguard ip>

Useful commands:
----------------
$ wg 
$ wg showconf <client> (e.g wei)


Sample of wireguard server
--------------------------
root@basecamp07:/home/basecamp# more /etc/wireguard/wg0.conf 
[Interface]
PrivateKey = WC6BHeV66Z+FAZfb0f1AR/bKAkzzr8VSPT/xy27I82g=
Address = 10.6.0.1/24
ListenPort = 51820
# begin wei
[Peer]
PublicKey = IPHEpZMQ/ZdpOQ/fOzpSN1LJWACH+ezKiBOZDbI7RRs=
PresharedKey = Oj2qO/oCSGr+o0pVaQJUuGypymo52e9pI51d7JJXEU8=
AllowedIPs = 10.6.0.2/32
# end wei

Sample of wireguard client
--------------------------
root@osboxes:/home/osboxes# more /etc/wireguard/wei.conf 
[Interface]
PrivateKey = cMHtC9s+REjCfMNtUmEHclUxiCQoXijHIlW0/WBKOUs=
Address = 10.6.0.2/24
DNS = 8.8.8.8, 8.8.4.4

[Peer]
PublicKey = z+d1yFVLf1ttFRlfwCot/HQ6sRq79f3YXpp+8N7kS28=
PresharedKey = Oj2qO/oCSGr+o0pVaQJUuGypymo52e9pI51d7JJXEU8=
Endpoint = <ip public>:51820
AllowedIPs = 0.0.0.0/0, ::0/0

