import scapy.all as scapy
from collections import defaultdict
import matplotlib.pyplot as plt
from IPython.display import display
import csv
import psutil
import os
import time

packet_count = 0
protocol_count = defaultdict(int)
packet_details = []

def packet_callback(packet):
    global packet_count
    global packet_details
    packet_count += 1
    
    if packet.haslayer(scapy.IP):
        ip_layer = packet.getlayer(scapy.IP)
        protocol = ip_layer.proto
        
        protocol_names = {
            1: "ICMP",
            2: "IGMP",
            6: "TCP",
            17: "UDP",
            41: "IPv6",
            50: "ESP",
            51: "AH",
            58: "ICMPv6"
        }
        
        protocol_name = protocol_names.get(protocol, "Unknown")
        protocol_count[protocol_name] += 1

        packet_info = {
            'No.': packet_count,
            'Time': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(packet.time)),
            'Source': ip_layer.src,
            'Destination': ip_layer.dst,
            'Protocol': protocol_name,
            'Length': len(packet)
        }
        packet_details.append(packet_info)

        print(f"Packet {packet_count}: {ip_layer.src} -> {ip_layer.dst} | Protocol: {protocol_name} | Size: {len(packet)} bytes | Time: {packet_info['Time']}")

def start_sniffing(interface):
    print(f"Starting packet capture on interface {interface}...")
    scapy.sniff(iface=interface, prn=packet_callback, store=0)

def display_statistics():
    global protocol_count, packet_details
    print("\n--- Protocol Statistics ---")
    
    for protocol, count in protocol_count.items():
        print(f"{protocol}: {count} packets")
    
    
    try:
        with open('protocol_statistics.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Protocol", "Count"])
            for protocol, count in protocol_count.items():
                writer.writerow([protocol, count])
        print("Statistics saved to 'protocol_statistics.csv'.")
    except Exception as e:
        print(f"Error saving statistics to CSV: {e}")
    
   
    if not packet_details:
        print("No packet details to save.")
        return

    protocols = list(protocol_count.keys())
    counts = list(protocol_count.values())

    plt.bar(protocols, counts)
    plt.xlabel('Protocol')
    plt.ylabel('Count')
    plt.title('Packet Protocol Distribution')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def list_network_interfaces():
    interfaces = psutil.net_if_addrs()
    print("Available interfaces:")
    for iface in interfaces:
        print(iface)

list_network_interfaces()


print()
print("Enter the interface name: ")
interface = input() 
try:
    start_sniffing(interface)
except KeyboardInterrupt:
    print("\nCapture stopped.")
    display_statistics()


csv_file = 'D:/4th semester/CN_EL/Working/Network_Traffic_Analyzer/protocol_statistics.csv'
try:
        with open(csv_file, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['No.',  'Time', 'Source', 'Destination', 'Protocol', 'Length'])
            writer.writeheader()
            writer.writerows(packet_details)
        print(f"Statistics saved to '{csv_file}'.")
except Exception as e:
        print(f"Error saving statistics to CSV: {e}")