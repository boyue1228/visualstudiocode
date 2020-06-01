# Readme of wireguard

=====================

## Requirements

1. Firewall open dst-nat to WireGuard server on UDP port 51820 (Mikortik)
2. WireGuard Server (10.67.19.200) - no lxc or vm machine.
3. WireGuard Client (ubuntu) - no lxc or vm machine

## Document references

- <https://github.com/pivpn/pivpn> (server installation)
- <https://www.wireguard.com/install/#ubuntu-1904-module-tools> (client installation)
- <https://wiki.archlinux.org/index.php/WireGuard> (concept and details, specailly on point-to-site routing paragraph)
- <https://stanislas.blog/2019/01/how-to-setup-vpn-server-wireguard-nat-ipv6/>
- <https://linuxize.com/post/how-to-set-up-wireguard-vpn-on-ubuntu-18-04/> (general tutorial)
- <https://engineerworkshop.com/blog/how-to-set-up-wireguard-on-a-raspberry-pi/#set-up-the-wireguard-client> （raspberry）
- <https://engineerworkshop.com/blog/how-to-set-up-a-wireguard-client-on-linux-with-conf-file/> （raspberry client)

If troubles on raspberry client installation, check the following and install kernel-headers

```$find /lib/modules -name wireguard.ko
$dpkg -s wireguard-tools
$dpkg -s wireguard-dkms
$dpkg -s raspberrypi-kernel
$dpkg -s raspberrypi-kernel-headers
$dkms status
```

## Installation

### Server

Interactive way, and following instruction

```$ curl -L <https://install.pivpn.io> | bash
$ pivpn -a -n (client)
$ pivpn list
$ pivpn remove
copy from ˜/configs/(xx).conf to each client

autostart

$ sudo systemctl enable wg-quick@wg0.service
$ sudo systemctl daemon-reload
$ sudo systemctl start wg-quick@wg0
$ systemctl status wg-quick@wg0

To remove service

$ sudo systemctl stop wg-quick@wg0
$ sudo systemctl disable wg-quick@wg0.service
$ sudo rm -i /etc/systemd/system/wg-quick@wg0
$ sudo systemctl daemon-reload
$ sudo systemctl reset-failed
```

### Client

```$ apt install resolvconf
$ mkdir -p /etc/wireguard
$ chown root:root /etc/wireguard
$ chmod 700 /etc/wireguard
$ cp (client).conf /etc/wireguard/
$ wg-quick up (client)
automatic restart :
$ sudo systemctl enable wg-quick@(client).service
$ sudo systemctl daemon-reload
$ sudo systemctl status wg-quick@wg0
```

### Mikrotik configuration

```IP/Firewall/NAT
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
$ ssh basecamp@10.6.0.1 <wireguard ip>
```

## Useful commands

```$ wg
$wg showconf <client> (e.g wei)
```

## Sample

### Wireguard server

```root@basecamp07:/home/basecamp# more /etc/wireguard/wg0.conf
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
```

### Wireguard client

```root@osboxes:/home/osboxes# more /etc/wireguard/wei.conf
[Interface]
PrivateKey = cMHtC9s+REjCfMNtUmEHclUxiCQoXijHIlW0/WBKOUs=
Address = 10.6.0.2/24
DNS = 8.8.8.8, 8.8.4.4

[Peer]
PublicKey = z+d1yFVLf1ttFRlfwCot/HQ6sRq79f3YXpp+8N7kS28=
PresharedKey = Oj2qO/oCSGr+o0pVaQJUuGypymo52e9pI51d7JJXEU8=
Endpoint = <ip public>:51820
AllowedIPs = 0.0.0.0/0, ::0/0
```

## Issues with resolvconf and solution

Disable and stop the systemd-resolved service:

```$sudo systemctl disable systemd-resolved
$ sudo systemctl stop systemd-resolved
Then put the following line in the [main] section of your /etc/NetworkManager/NetworkManager.conf:
    dns=default
Delete the symlink /etc/resolv.conf
$ rm /etc/resolv.conf
Restart NetworkManager
$ sudo systemctl restart NetworkManager
```

## wireguard for proxmox lxc container

1. <https://nixvsevil.com/posts/wireguard-in-proxmox-lxc/>

## Ceph storage

1. sgdisk -Z /dev/sdb  and repeat for /dev/sdc
2. ceph fs rm cephfs --yes-i-really-mean-it
3. go to pools -> destroy cephfs_data nad cephfs_metadata

there are also points that i would like to see on "howto" / best practices to make a clean network/setup/production design. Security is not only penetration of hacker, but security on what kind of things that we could do to prevent our network/setup when user do error (that happens anyway)

docker run --rm -it --name node-docker \
-v $PWD:/home/wei/node-docker -w /home/wei/node-docker \
-e "PORT=3000" -p 8888:3000  \
-u node node:latest /bin/bash

docker run --rm -it --name node-docker \
-v $PWD:/home/wei/node-docker -p 8888:3000 \
node-docker

docker-compose run --rm --service-ports nod_dev_env


 "completeHTMLDocument": false,
    "encodeEmails": true,
    "ghCodeBlocks": true,
    "ghCompatibleHeaderId": true,
    "headerLevelStart": 3,
    "openLinksInNewWindow": true,
    "simpleLineBreaks": true,
    "simplifiedAutoLink": true,
    "strikethrough": true,
    "tables": true,
    "tasklists": true