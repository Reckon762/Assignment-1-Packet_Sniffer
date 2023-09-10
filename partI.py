import socket
import struct
import csv

# Create a CSV file for storing flow information
csv_file = open('unique-IPs.csv', mode='w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Source IP', 'Source Port', 'Destination IP', 'Destination Port', 'Protocol'])

# Create a dictionary to store unique flows
unique_flows = {}

def packet_sniffer():
    # Create a raw socket and bind it to the 'eth0' interface
    sniffer = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(3))
    sniffer.bind(("eth0", 0))

    try:
        while True:
            # Capture a packet
            packet_data = sniffer.recvfrom(65535)[0]

            # Parse Ethernet header
            eth_header = struct.unpack('!6s6sH', packet_data[:14])
            eth_type = eth_header[2]

            # Check if the packet is an IPv4 packet
            if eth_type == 0x0800:  # 0x0800 indicates an IPv4 packet
                # Parse IP header
                ip_header = struct.unpack('!BBHHHBBH4s4s', packet_data[14:34])
                protocol = ip_header[6]
                src_ip = socket.inet_ntoa(ip_header[8])
                dst_ip = socket.inet_ntoa(ip_header[9])

                # Check if the packet is a TCP packet
                if protocol == 6:  # 6 indicates TCP
                    # Parse TCP header
                    tcp_header = struct.unpack('!HHLLBBHHH', packet_data[34:54])
                    src_port = tcp_header[0]
                    dst_port = tcp_header[1]

                    # Create a unique flow key as a tuple
                    flow_key = (src_ip, src_port, dst_ip, dst_port, "TCP")

                    # Check if this flow is unique (not in the dictionary)
                    if flow_key not in unique_flows:
                        # Write flow information to the CSV file
                        flow_info = [src_ip, src_port, dst_ip, dst_port, "TCP"]
                        csv_writer.writerow(flow_info)

                        # Add the flow to the dictionary to mark it as seen
                        unique_flows[flow_key] = True

    except KeyboardInterrupt:
        print("\nPacket capture stopped.")
        csv_file.close()

if __name__ == "__main__":
    packet_sniffer()
