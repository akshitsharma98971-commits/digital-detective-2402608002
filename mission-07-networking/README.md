# Mission 7 - How computers communicate

## 1. Task / objective
The objective of this mission was to learn fundamental computer networking concepts, test basic network connectivity and domain lookups from the terminal, and explain step by step what happens behind the scenes when a user visits a website in a browser.

## 2. Work completed
I wrote explanations and simple examples for eight key networking concepts: LAN, MAN, WAN, DNS, Router, Protocol, Packet switching, and Client-server.
I ran network diagnostic commands in the terminal (ping and nslookup) using the public website example.com.
I saved safe command output into evidence/mission-07-network-log.txt without including private network details like personal IP or Wi-Fi names.
I wrote a numbered 6-step guide describing how a client browser loads a web page from a web server using DNS, routers, and protocols.

## 3. Commands / tools used
ping -c 4 example.com: sent 4 network packets to example.com to check if the remote server was reachable and measured response time.
nslookup example.com: asked a DNS server to look up the IP address for the domain name example.com.

## 4. My understanding

Task 7.1 - Explain network concepts

1. LAN (Local Area Network)
- Explanation: A network of connected devices that covers a small, limited physical area like a home, school computer lab, or office room.
- Example: The Wi-Fi network in my house that connects my laptop, phone, and home printer.

2. MAN (Metropolitan Area Network)
- Explanation: A network that spans a larger area than a LAN, such as an entire town, city, or large university campus.
- Example: A city cable television network or a network connecting several college buildings across a city.

3. WAN (Wide Area Network)
- Explanation: A very large network that covers huge geographical distances, such as across different states, countries, or the whole globe.
- Example: The global Internet is the most well-known example of a WAN.

4. DNS (Domain Name System)
- Explanation: A phonebook system for computers that translates human-friendly website names into numeric IP addresses that computers need to find each other.
- Example: Translating google.com into an IP address like 142.250.190.46.

5. Router
- Explanation: A networking device that connects different computer networks together and directs data packets toward their destination.
- Example: The Wi-Fi router in my home that routes internet traffic between my laptop and the internet service provider.

6. Protocol
- Explanation: An agreed set of rules and standards that devices must follow so they can understand each other and exchange information properly.
- Example: HTTPS, which is the secure protocol used by web browsers to request and receive web pages.

7. Packet switching
- Explanation: A communication technique where data (like a file or message) is broken down into small individual chunks called packets, sent across various network paths, and reassembled at the destination.
- Example: Downloading an image on the web where the image is broken into small packets and reconstructed in order on your screen.

8. Client-server
- Explanation: A structure where one device or program (the client) asks for information or services, and another computer (the server) listens for requests and serves the response back.
- Example: My web browser acting as a client requesting a video page from YouTube's server.

Task 7.2 - Observe network information

Terminal test results:
- ping -c 4 example.com: Transmitted 4 packets and received 4 packets back with 0.0% packet loss. Average response time was around 9 milliseconds.
- nslookup example.com: Asked DNS server (8.8.8.8) and received IPv4 addresses 172.66.147.243 and 104.20.23.154 for example.com.

Questions answered:
1. Explain what a connectivity test helps you check:
Running a connectivity test like ping helps check whether your computer can successfully reach a remote server across the network. It tells you if the connection is active, whether any data packets got lost along the way, and how long it takes for a signal to go there and come back (latency).

2. Explain what information a DNS lookup displays:
A DNS lookup tool like nslookup shows the domain name you queried, the DNS server that handled the lookup, and the actual numeric IP address (or addresses) connected to that domain name.

3. Describe the role of DNS when you enter a website name in a browser:
When you type a domain name like example.com in a web browser, the browser does not know which physical computer in the world hosts that site. DNS acts as a directory: the browser asks the DNS server for the IP address belonging to that name, and once DNS returns the number, the browser can send its web request directly to that server.

Task 7.3 - What happens when you open a website?
Here is what happens in 6 steps when a user opens a web page:

1. The user types a website address (such as https://example.com) into the client browser address bar and hits Enter.
2. The browser checks its local cache and then queries a DNS server to resolve the domain name into an IP address.
3. The DNS server replies with the server's numerical IP address.
4. The client browser establishes a connection with the web server at that IP address using standard protocols (TCP/IP and secure TLS/HTTPS handshake) guided by intermediate routers.
5. Once connected, the client browser sends an HTTP GET request asking for the webpage files.
6. The web server processes the request, locates the web page files, and sends an HTTP response back with the HTML, CSS, and image data. The client browser reads this response and renders the finished web page on the screen for the user to see.

## 5. Difficulties faced
When looking at ping output, the terms like ttl and time=7.791 ms were slightly confusing at first. Also, understanding why a website might have multiple IP addresses returned by nslookup took some reading.

## 6. How I resolved them
I learned that ms stands for milliseconds and measures latency (round trip speed), and that larger websites return multiple IP addresses so they can distribute traffic across multiple servers for reliability.

## 7. Evidence / files
- evidence/mission-07-network-log.txt: terminal output from running ping and nslookup.
- mission-07-networking/README.md: notes on network terms and website loading steps.

## 8. Commit details
Commit message: Explain networking concepts and website communication
Committed and pushed to GitHub.
