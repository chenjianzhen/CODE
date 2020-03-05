# -*- coding=utf-8 -*-
"""
-------------------------------
    Project:    AI
    File Name:  learn-scrapy.py
    Description:
    Author:     Administrator
    Date:       2020/03/04
    Time:       12:22
-------------------------------
    Modify Activity:
                2020/03/04
-------------------------------
"""
__author__ = 'Administrator'

from scapy.all import *

def packet_callback(packet):

    print(packet.show())
    if packet[TCP].payload:
        mail_packet = str(packet[TCP].payload)

        if "user" in mail_packet.lower() or "pass" in mail_packet.lower():
            print("[*] Server: %s" % packet[IP].dst)
            print("[*]  %s" % packet[TCP].payload)

sniff(filter="tcp port 110 or tcp port 25 or tcp port 143",
      prn=packet_callback,
      store=0)


