import socket
import struct
import time
import subprocess

# This set will store rows we've already seen
unique_flows = set()

def get_mac_addr(bytes_addr):
    bytes_str = map('{:02x}'.format, bytes_addr)
    mac_addr = ':'.join(bytes_str).upper()
    return mac_addr

def get_pid_using_port(port):
    try:
        result = subprocess.check_output(['lsof', '-i', f':{port}', '-n', '-P'])
        lines = result.decode().split('\n')
        if len(lines) > 1:
            pid = lines[1].split()[1]
            return pid
    except subprocess.CalledProcessError:
        pass
    return None

# filename = "ip_store.csv"

# with open(filename, 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(['Source IP', 'Source Port', 'Destination IP', 'Destination Port', 'Protocol'])
s = socket.socket(socket.PF_PACKET,socket.SOCK_RAW,socket.ntohs(3))


start_time = time.time()
while time.time() - start_time < 30:
    packet = s.recvfrom(65565)
    raw_data,addr = packet

    ethernet_header = raw_data[0:14]
    s_mac, d_mac, _ = struct.unpack("!6s6s2s", ethernet_header)

    s_mac = get_mac_addr(s_mac)
    d_mac = get_mac_addr(d_mac)

    ip_header = raw_data[14:34]
    version_ihl, tos, total_length, id, flags_fragment, ttl, protocol, checksum, src_ip, dst_ip = struct.unpack('!BBHHHBBH4s4s', ip_header)
    src_port, dst_port = struct.unpack('!HH', raw_data[34:38])

    # Append to CSV file if protocol is TCP
    # if protocol == 6:
    #     if(socket.inet_ntoa(src_ip) != "10.0.2.15" and socket.inet_ntoa(dst_ip) != "10.0.2.15"):
    #         with open(filename, 'a', newline='') as csvfile:
    #             writer = csv.writer(csvfile)

    #             flow = tuple([socket.inet_ntoa(src_ip), src_port, socket.inet_ntoa(dst_ip), dst_port, "TCP"])

    #             if flow not in unique_flows:
    #                 unique_flows.add(flow)
    #                 writer.writerow([socket.inet_ntoa(src_ip), src_port, socket.inet_ntoa(dst_ip), dst_port, "TCP"])
    
    print('Destination Mac_Address: {}, Source Mac_Address: {}'.format(s_mac, d_mac)) 
    print("Source IP:" + socket.inet_ntoa(src_ip) + " Source Port:" + str(src_port) + " Destination IP:" + socket.inet_ntoa(dst_ip) + " Destination port:" + str(dst_port) + " Length:" + str(len(raw_data)))

print("\n\nFinished sniffing packets for 30 seconds.\n")

# Prompt for port and print the PID
try:
    while True:
        port = input("Enter the port number: ")
        pid = get_pid_using_port(port)
        if pid:
            print(f"Process ID for port {port}: {pid}")
        else:
            print(f"No process found using port {port}.")
except KeyboardInterrupt:
    print("\nExiting the program.")