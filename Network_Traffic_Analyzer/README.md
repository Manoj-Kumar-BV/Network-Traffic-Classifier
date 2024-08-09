---

# Network Traffic Analyzer

This project is a simple network traffic analyzer using Python and the Scapy library. The analyzer captures network packets on a specified interface, extracts information such as source and destination IP addresses, protocol, and packet size, and then provides statistics on the captured data.

## Features

- Captures network packets in real-time.
- Extracts and displays details such as source IP, destination IP, protocol type, and packet size.
- Counts the number of packets for each protocol type.
- Saves the protocol statistics to a CSV file.
- Saves detailed packet information to a CSV file.
- Displays a bar chart showing the distribution of different protocols in the captured traffic.

## Requirements

Before running the script, ensure you have the following Python packages installed:

- `scapy`
- `psutil`
- `matplotlib`

You can install these dependencies using pip:

```bash
pip install scapy psutil matplotlib
```

## How to Use

### 1. Listing Network Interfaces

The script begins by listing all available network interfaces on your system. You will be prompted to choose an interface for packet capturing.

```python
list_network_interfaces()
```

### 2. Starting Packet Capture

Once you have selected the interface, the script will begin capturing packets on that interface. The captured packets are processed in real-time, displaying the following information:

- Source IP address
- Destination IP address
- Protocol (e.g., TCP, UDP, ICMP)
- Packet size
- Capture timestamp

The packet capture continues until you manually stop it using `Ctrl + C`.

```python
start_sniffing(interface)
```

### 3. Displaying and Saving Statistics

When you stop the packet capture, the script displays statistics for each protocol and saves these statistics to a CSV file (`protocol_statistics.csv`). It also saves the detailed packet information to another CSV file.

```python
display_statistics()
```

The protocol distribution is also visualized using a bar chart.

### 4. Output Files

The script generates the following output files:

- `protocol_statistics.csv`: Contains the count of packets for each protocol.
- `packet_details.csv`: Contains detailed information about each captured packet.

The files are saved in the directory specified in the script.

## Customization

If you wish to change the location where the CSV files are saved, you can modify the `csv_file` variable in the script:

```python
csv_file = 'path/to/your/directory/protocol_statistics.csv'
```

## Example Usage

1. Run the script:

```bash
python network_traffic_analyzer.py
```

2. Select the network interface when prompted.
3. Monitor the real-time packet information.
4. Stop the capture using `Ctrl + C`.
5. View the saved CSV files and bar chart.

---
