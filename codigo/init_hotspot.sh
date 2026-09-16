#!/usr/bin/bash


nmcli device status
nmcli radio wifi
sudo nmcli device wifi hotspot ifname wlan1 con-name CarroZ ssid CarroZ password Zanardi2026
sudo nmcli connection modify CarroZ ipv4.method shared ipv4.addresses 10.0.0.1/24
sudo nmcli connection modify CarroZ connection.autoconnect yes
nmcli device status
ifconfig
#sudo nmcli connection modify CarroZ ipv4.method shared ipv4.address 10.0.0.1/24
#sudo nmcli connection down CarroZ
#sudo nmcli connection up CarroZ
#ifconfig
ip addr show wlan1

