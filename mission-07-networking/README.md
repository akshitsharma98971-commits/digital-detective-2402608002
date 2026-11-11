# Mission 7 — How computers communicate

## 1. Task / objective
The objective of Mission 7 is to explore computer networking fundamentals: defining foundational network topologies and communication protocols, observing remote connectivity and Domain Name System (DNS) address resolution in Terminal, and formulating a comprehensive end-to-end trace of what occurs under the hood when a user loads a website in a web browser.

## 2. Work completed
- Analyzed and formulated explanations and examples for 8 foundational network concepts (LAN, MAN, WAN, DNS, Router, Protocol, Packet Switching, Client-Server model).
- Conducted live terminal network diagnostics using `ping` and `nslookup` against `example.com`.
- Preserved privacy-safe terminal telemetry in `evidence/mission-07-network-log.txt`.
- Drafted a rigorous 7-step walkthrough detailing how clients, DNS servers, routers, protocols (HTTP/HTTPS, TCP/IP), and web servers interact during website retrieval.
- Documented findings in `mission-07-networking/README.md`.

---

## 3. Commands / tools used
| Command / Tool | Purpose | Output / Observation |
| :--- | :--- | :--- |
| `ping -c 4 example.com` | Test end-to-end ICMP echo reachability, packet loss, and round-trip latency to a remote server | Transmitted 4 packets, received 4 packets (0.0% packet loss), average latency: `9.021 ms`. |
| `nslookup example.com` | Query the Domain Name System (DNS) to resolve a domain name into its corresponding IP addresses | Resolved `example.com` to IPv4 addresses `172.66.147.243` and `104.20.23.154` via resolver `8.8.8.8`. |

---

## 4. My understanding

### Task 7.1 — Explain network concepts

| Concept | Explain it in your own words | Example |
| :--- | :--- | :--- |
| **LAN (Local Area Network)** | A localized computer network restricted to a small, distinct geographic boundary such as a single home, classroom, computer laboratory, or office suite. | A home Wi-Fi network connecting your personal laptop, smartphone, and wireless printer. |
| **MAN (Metropolitan Area Network)** | A high-bandwidth network infrastructure spanning an entire town, city, or extensive university campus, interconnecting multiple LANs. | A municipal fiber-optic network connecting civic government buildings, police stations, and libraries across Bangalore. |
| **WAN (Wide Area Network)** | A geographically dispersed telecommunications network that spans across regions, states, nations, or globally across continents. | The global Internet itself, or a multinational corporation's intercontinental private leased-line network. |
| **DNS (Domain Name System)** | The distributed naming directory of the Internet that translates human-friendly alphanumeric domain names into machine-routable numerical IP addresses. | Translating `google.com` or `github.com` into an IPv4 address like `142.250.190.46`. |
| **Router** | A specialized networking hardware device that directs and forwards data packets between different IP subnets based on routing tables and packet destination headers. | A home gateway router connecting your domestic local Wi-Fi subnet to your Internet Service Provider's (ISP) external WAN network. |
| **Protocol** | A standardized set of syntactic, semantic, and synchronizing rules governing how computing devices format, transmit, and handle data across a network. | **HTTPS** (Hypertext Transfer Protocol Secure), **TCP** (Transmission Control Protocol), and **IP** (Internet Protocol). |
| **Packet switching** | A data transmission technique where digital messages are decomposed into discrete, numbered chunks (packets) that travel independently across available network routes before being reassembled at the destination. | Transmitting a 10 MB image file over the Internet as thousands of individual 1500-byte IP packets that traverse diverse internet routers. |
| **Client-server** | A distributed computing architecture where service requestors (clients) initiate requests for information or resources, and centralized providers (servers) fulfill those requests. | Your web browser (the client) requesting a web page from a GitHub web host (the server). |

---

### Task 7.2 — Observe network information
- **What a connectivity test (`ping`) helps check:**
  A connectivity test verifies whether an active, bidirectional communication path exists between your local computer and a remote host. By transmitting ICMP Echo Request packets and measuring incoming Echo Replies, it identifies whether the destination host is reachable, checks for network packet loss (unstable links), and measures latency (round-trip time in milliseconds).
- **What information a DNS lookup (`nslookup`) displays:**
  A DNS lookup displays which DNS resolver server handled the query (e.g. `8.8.8.8#53`), whether the answer is authoritative or cached, the canonical hostname requested, and the resolved numerical IP addresses (such as `172.66.147.243` and `104.20.23.154`) that identify the web server on the Internet.
- **The role of DNS when entering a website name in a browser:**
  Humans navigate the web using intuitive textual names like `example.com`, but the underlying Internet Protocol (IP) routing hardware can only route packets using numerical IP addresses. DNS acts as an essential lookup directory: before your browser can request any data, it consults DNS to convert the textual domain into its target IP address so network connections can be opened.

---

### Task 7.3 — What happens when you open a website?
When a user enters a website URL (such as `https://example.com`) into a browser address bar and hits Enter, the following sequence takes place:

1. **Step 1: User Input and Local Cache Inspection (Client)**  
   The user enters `https://example.com` into the web browser (the **client**). The browser checks its internal caches (browser cache, operating system DNS cache, and local hosts file) to see if the corresponding IP address was recently stored.
2. **Step 2: DNS Resolution Request (DNS Query)**  
   If the IP address is not cached, the client dispatches a recursive **DNS** query over the UDP **protocol** to the configured recursive resolver (such as `8.8.8.8` or the local ISP resolver). The resolver traverses the DNS hierarchy (Root servers $\rightarrow$ `.com` TLD servers $\rightarrow$ Authoritative Name Servers) to obtain the server's numerical IP address (`172.66.147.243`) and returns it to the client.
3. **Step 3: Network Routing and Gateway Traversal (Network / Router)**  
   Armed with the server IP address, the client creates network connection packets. The local computer sends these packets across the local Wi-Fi/Ethernet link to the default gateway **router**. The router consults its routing table and forwards the packet onto the ISP's wide-area network (WAN) toward the target destination.
4. **Step 4: Transport Handshake Establishment (Protocol / TCP & TLS)**  
   The client initiates a connection with the remote **server** using the Transmission Control **Protocol** (TCP). Through a 3-way handshake (`SYN`, `SYN-ACK`, `ACK`), a reliable session is established. Because the URL specified `https://`, an additional cryptographic TLS handshake takes place to authenticate the server certificate and establish an encrypted session key.
5. **Step 5: Client Request Transmission (HTTP GET)**  
   Over the encrypted channel, the **client** browser transmits an HTTP request message (`GET / HTTP/1.1`) identifying the requested page, accepted formats, and client metadata headers.
6. **Step 6: Server Processing and Response (Server)**  
   The web **server** listening at the destination IP address receives the request packets, processes the requested resource (fetching HTML, CSS, JavaScript, or querying databases), and formulates an HTTP response packet containing a status code (e.g., `200 OK`) and the requested payload data.
7. **Step 7: Packet Switching and Rendering (Client Display)**  
   The server's response packets travel back through intermediary **routers** via packet switching to the client. The browser client reassembles the packets, parses the HTML DOM tree, applies CSS styling rules, runs JavaScript code, and visually renders the interactive website on the user's screen.

---

## 5. Difficulties faced
- Differentiating between the transport layer (TCP/IP) packet transmission and application layer (HTTP/HTTPS) protocol requests.

## 6. How I resolved them
- Reviewed the OSI and TCP/IP layered networking models, mapping how lower-level protocols carry application-level HTTP data inside IP packet payloads.

## 7. Evidence / files
- Privacy-safe network trace log: `evidence/mission-07-network-log.txt`
- Documentation: `mission-07-networking/README.md`

## 8. Commit details
- **Commit Message:** `Explain networking concepts and website communication`
- **Pushed to GitHub:** Yes (Branch: `main`)
