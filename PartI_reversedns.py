import csv
import socket

# Function for reverse DNS lookup
def reverse_dns_lookup(ip_address):
    try:
        hostnames = socket.gethostbyaddr(ip_address)
        primary_hostname = hostnames[0]
        return primary_hostname
    except socket.herror:
        return "N/A"

# Read source and destination IP addresses from unique_IPs.csv
source_ips = []
destination_ips = []
current_category = None

with open('unique-IPs.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    for row in csv_reader:
        if len(row) == 0:
            continue  # Skip empty lines

        if row[0] == 'Source IP':
            current_category = source_ips
        elif row[0] == 'Destination IP':
            current_category = destination_ips
        else:
            current_category.append(row[0])

# Create a new CSV file and write the rows
with open('PartI_reversedns.csv', mode='w', newline='') as csv_file:
    fieldnames = ['IP', 'Hostname']
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

    # Write source IP addresses and their DNS
    for source_ip in source_ips:
        hostname = reverse_dns_lookup(source_ip)
        csv_writer.writerow({'IP': source_ip, 'Hostname': hostname})

    # Write destination IP addresses and their DNS
    for destination_ip in destination_ips:
        hostname = reverse_dns_lookup(destination_ip)
        csv_writer.writerow({'IP': destination_ip, 'Hostname': hostname})
