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

All the hostnames and their IPs can be seen from the CSV file. However below are the 5 hostnames with the IPs.
1. 18.164.246.94	server-18-164-246-94.del54.r.cloudfront.net
2. 


### Part II
The sum of our roll number is 144 + 93 = 237 and 237 mod 4 gives 1. 
Thus, we have used the 1.pcap file for this part.

1. Open 2 terminals and run the Python script **partII.py** in one terminal (use command: **sudo python PartII.py**)
2. Simultaneously run the command **sudo tcpreplay -i --mbps=1 -v 1.pcap** in other terminal. 
3. The packets replayed using the tcpreplay command are captured by the raw socket.
4. The Python script partII.py stores all the packet payload in **PartII_allparts.csv** as per the requirements.
   
**Answers:** <br>
**a.** There is a Flag in a TCP Packet. Identify the flag. : **Romeo** <br>
**b.** My username is secret, Identify my secret. : **I find a way, not a excuse.** <br>
**c.** I have a TCP checksum “0x0ac4”. I have instructions in my path. : **GET /your-password-is-somewhere-in--this-stream HTTP/1.1** & **GET / HTTP/1.1 Origin: www.cs433.com User-Agent: PASSWORD-Berlin** <br>
**d.** My device has an IP Address “131.144.126.118”. Sum of my connection ports will lead you to a person. : **The person you are looking for is Rabindranath Tagore** <br>
**e.** I come from localhost, I requested a milkshake. Find my flavour. : **flavor- Strawberry** <br>


### Part III
1. Open the terminal and run the Python script **partIII.py**. Also, keep doing the normal network activities so the that program can capture the packets.
2. After 30 seconds, the program will stop capturing the packets and a prompt to enter the port number.
3. Look from the packet captured previously for the port numbers.
4. Enter the port number and hit enter.
5. If the activity is still going on that port, a process ID will be generated corresponding to that port.
6. The prompt will again ask for port number to enter and will do so until CTRL+C is executed to terminate the program.
