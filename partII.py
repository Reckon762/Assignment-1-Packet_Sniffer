# import socket
# import struct
# import binascii

# def main():
#     # Create a raw socket to capture packets
#     raw_socket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x0003))

#     while True:
#         # Receive a packet (maximum 65535 bytes)
#         packet, _ = raw_socket.recvfrom(65535)

#         # Check if the packet contains IP and TCP headers
#         if len(packet) >= 54:  # Assuming minimum Ethernet frame size
#             ethernet_header = packet[:14]
#             ip_header = packet[14:34]  # Assuming IPv4 headers are 20 bytes

#             # Check if the IP packet contains a TCP segment
#             if ip_header[9] == 6:  # 6 corresponds to TCP
#                 tcp_header = packet[34:54]  # Assuming TCP headers are 20 bytes
#                 tcp_data = packet[54:]  # Payload starts after the TCP header

#                 # Extract the TCP checksum from the header
#                 tcp_checksum = struct.unpack('!H', tcp_header[16:18])[0]

#                 # Check if the TCP checksum matches the desired value (0xf436)
#                 if tcp_checksum == 0xf436:
#                     # Convert the payload to ASCII text
#                     try:
#                         ascii_data = tcp_data.decode('utf-8', errors='replace')
#                     except UnicodeDecodeError:
#                         ascii_data = binascii.hexlify(tcp_data).decode('utf-8', errors='replace')

#                     # Print the payload
#                     print("\nTCP Checksum: ")
#                     print(f"Hexadecimal Value: 0x{tcp_checksum:04X}")
#                     print("\nTCP Payload:")
#                     print(ascii_data)

# if __name__ == "__main__":
#     main()

# import socket
# import struct
# import csv

# # Create a CSV file for storing flow information
# csv_file = open('flows.csv', mode='w', newline='')
# csv_writer = csv.writer(csv_file)
# csv_writer.writerow(['Source IP', 'Source Port', 'Destination IP', 'Destination Port', 'Protocol'])

# # Create a dictionary to store unique flows
# unique_flows = {}

# def packet_sniffer():
#     # Create a raw socket and bind it to the 'eth0' interface
#     sniffer = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(3))
#     sniffer.bind(("eth0", 0))

#     try:
#         while True:
#             # Capture a packet
#             packet_data = sniffer.recvfrom(65535)[0]

#             # Parse Ethernet header
#             eth_header = struct.unpack('!6s6sH', packet_data[:14])
#             eth_type = eth_header[2]

#             # Check if the packet is an IPv4 packet
#             if eth_type == 0x0800:  # 0x0800 indicates an IPv4 packet
#                 # Parse IP header
#                 ip_header = struct.unpack('!BBHHHBBH4s4s', packet_data[14:34])
#                 protocol = ip_header[6]
#                 src_ip = socket.inet_ntoa(ip_header[8])
#                 dst_ip = socket.inet_ntoa(ip_header[9])

#                 # Check if the packet is a TCP packet
#                 if protocol == 6:  # 6 indicates TCP
#                     # Parse TCP header
#                     tcp_header = struct.unpack('!HHLLBBHHH', packet_data[34:54])
#                     src_port = tcp_header[0]
#                     dst_port = tcp_header[1]

#                     # Check if the TCP checksum matches the desired value (0xf436)
#                     if tcp_header[7] == 0xf436:
#                         # Create a unique flow key as a tuple
#                         flow_key = (src_ip, src_port, dst_ip, dst_port, "TCP")

#                         # Check if this flow is unique (not in the dictionary)
#                         if flow_key not in unique_flows:
#                             # Write flow information to the CSV file
#                             flow_info = [src_ip, src_port, dst_ip, dst_port, "TCP"]
#                             csv_writer.writerow(flow_info)

#                             # Add the flow to the dictionary to mark it as seen
#                             unique_flows[flow_key] = True

#     except KeyboardInterrupt:
#         print("\nPacket capture stopped.")
#         csv_file.close()

# if __name__ == "__main__":
#     packet_sniffer()


# import socket
# import struct
# import csv

# # Create a CSV file for storing flow information
# csv_file = open('TCP-checksum.csv', mode='w', newline='')
# csv_writer = csv.writer(csv_file)
# csv_writer.writerow(['Source IP', 'Source Port', 'Destination IP', 'Destination Port', 'Protocol', 'TCP Checksum'])

# # Create a dictionary to store unique flows
# unique_flows = {}

# def packet_sniffer():
#     # Create a raw socket and bind it to the 'eth0' interface
#     sniffer = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(3))
#     sniffer.bind(("eth0", 0))

#     try:
#         while True:
#             # Capture a packet
#             packet_data = sniffer.recvfrom(65535)[0]

#             # Parse Ethernet header
#             eth_header = struct.unpack('!6s6sH', packet_data[:14])
#             eth_type = eth_header[2]

#             # Check if the packet is an IPv4 packet
#             if eth_type == 0x0800:  # 0x0800 indicates an IPv4 packet
#                 # Parse IP header
#                 ip_header = struct.unpack('!BBHHHBBH4s4s', packet_data[14:34])
#                 protocol = ip_header[6]
#                 src_ip = socket.inet_ntoa(ip_header[8])
#                 dst_ip = socket.inet_ntoa(ip_header[9])

#                 # Check if the packet is a TCP packet
#                 if protocol == 6:  # 6 indicates TCP
#                     # Parse TCP header
#                     tcp_header = struct.unpack('!HHLLBBHHH', packet_data[34:54])
#                     src_port = tcp_header[0]
#                     dst_port = tcp_header[1]
#                     tcp_checksum = hex(tcp_header[7])
#                     # cat TCP-checksum.csv | grep 0xf436
#                     # 199.194.191.199,919,108.103.101.100,1003,TCP,0xf436

#                     # Create a unique flow key as a tuple
#                     flow_key = (src_ip, src_port, dst_ip, dst_port, "TCP")

#                     # Check if this flow is unique (not in the dictionary)
#                     if flow_key not in unique_flows:
#                         # Write flow information to the CSV file
#                         flow_info = [src_ip, src_port, dst_ip, dst_port, "TCP", tcp_checksum]
#                         csv_writer.writerow(flow_info)

#                         # Add the flow to the dictionary to mark it as seen
#                         unique_flows[flow_key] = True

#     except KeyboardInterrupt:
#         print("\nPacket capture stopped.")
#         csv_file.close()

# if __name__ == "__main__":
#     packet_sniffer()

import socket
import struct
import csv
import string

# def is_valid_ascii(data):
#     try:
#         # Convert the data bytes to a string and check if it's valid ASCII
#         data_str = data.decode('utf-8', errors='strict')
#         return all(c in string.printable for c in data_str)
#     except UnicodeDecodeError:
#         return False
    

def is_valid_ascii(data):
    try:
        # Convert the data bytes to a string and check if it's valid ASCII
        data_str = data.decode('utf-8', errors='backslashreplace')
        return all(c in string.printable for c in data_str)
    except UnicodeDecodeError:
        return False

# Create a CSV file for storing flow information
csv_file = open('all-packets.csv', mode='w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Source IP', 'Source Port', 'Destination IP', 'Destination Port', 'Protocol', 'TCP Checksum', 'Payload (text)'])

# Create a dictionary to store all flows
all_flows = {}

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

                # Check if the packet is a TCP or UDP packet
                if protocol == 6 or protocol == 17:
                    # Parse TCP or UDP header
                    tcp_header = struct.unpack('!HHLLBBHHH', packet_data[34:54])
                    src_port = tcp_header[0]
                    dst_port = tcp_header[1]
                    tcp_checksum = hex(tcp_header[7])

                    # Create a unique flow key as a tuple
                    flow_key = (src_ip, src_port, dst_ip, dst_port, protocol)

                    # Add the flow to the dictionary
                    all_flows[flow_key] = True

                    # Get the payload
                    tcp_payload = packet_data[54:]
                    print(type(tcp_payload))
                    # Convert the payload to text
                    if is_valid_ascii(tcp_payload):
                        # Print the TCP payload in text format
                        # print("\nTCP Payload (Text):")
                        # print(tcp_payload.decode('utf-8'))
                        hex_string = tcp_payload
                        ascii_value = tcp_payload.decode('utf-8', errors='backslashreplace')
                        flow_info = [src_ip, src_port, dst_ip, dst_port, protocol, tcp_checksum, ascii_value]
                        csv_writer.writerow(flow_info)
                    
                    # else:
                    # # # Write flow information to the CSV file
                    #     # flow_info = [src_ip, src_port, dst_ip, dst_port, protocol, tcp_checksum, "NAN"]
                    #     csv_writer.writerow(flow_info)

    except KeyboardInterrupt:
        print("\nPacket capture stopped.")
        csv_file.close()

if __name__ == "__main__":
    packet_sniffer()
