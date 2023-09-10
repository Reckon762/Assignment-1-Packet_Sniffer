# Assignment-1 Computer Networks 

Team Members :
1. Pratik Raj     20110144
2. Karan Bhardwaj 20110093

## Instructions to run the code

### Part I
The sum of our roll number is 144 + 93 = 237 and 237 mod 3 gives 0. 
Thus, we have used the 0.pcap file for this part.
1. Open 2 terminals and run the Python script **partI.py** in one terminal (use command: **sudo python PartI.py**)
2. Simultaneously run the command **sudo tcpreplay -i --mbps=1 -v 0.pcap** in other terminal. 
3. The packets replayed using the tcpreplay command are captured by the raw socket.
4. The Python script partI.py stores all the unique flows in **unique-IPs.csv**.
5. The CSV file contains the source IP, destination IP, source port, destination port, and protocol for each unique flow.

Now, for obtaining the Reverse DNS of IP addresses.
1. Run the Python script **partI_reversedns.py** using the command **sudo python partI_reversedns.py** to get the hostname of all IPs present in the unique flow.
2. All the hostnames along the IPs get saved in the **PartI_reversedns.csv** file.

