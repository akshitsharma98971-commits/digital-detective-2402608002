# The Digital Detective: Explore Your Computer • Build a Mini System Report

**Diwali Independent Learning Assignment**

## Student Information
- **Name:** Akshit Sharma
- **USN:** 2402608002
- **Campus / Section:** NST Bangalore
- **GitHub Username:** akshitsharma98971-commits
- **GitHub Repository Name:** `digital-detective-2402608002`
- **GitHub Repository URL:** [https://github.com/akshitsharma98971-commits/digital-detective-2402608002](https://github.com/akshitsharma98971-commits/digital-detective-2402608002)

---

## Assignment Overview
The **Digital Detective** assignment is an intensive, practical investigation into the foundational layers of computing systems, operating systems, software execution, data representation, version control, and computer networking. 

Across nine sequential missions, this project explores how physical hardware coordinates with kernel software, how command-line interfaces enable safe systems management, how compilers and interpreters differ, how binary and hexadecimal numbers represent information, how Git branching and Pull Requests enable collaborative software engineering, and how the Internet delivers web resources from servers to clients.

---

## Topics Explored
1. **Computer Fundamentals & the IPOS Model:** Tracking data flow across Input, Processing, Output, and Storage stages; classifying system, application, and utility software; analyzing everyday embedded systems (ATMs, traffic lights, smart transit gates).
2. **Command-Line & Terminal Proficiency:** Navigating hierarchical filesystems, executing safe file operations, appending vs. overwriting streams (`>>` vs `>`), combining commands with Unix pipes (`|`), and using package managers (Homebrew).
3. **Operating System Architecture & Internals:** Inspecting hardware platforms, kernel releases, storage quotas, tracking processes and PIDs, evaluating absolute vs. relative paths, and decoding POSIX file permission triples (`rwx`).
4. **Program Execution & Language Translation:** Executing Python scripts and conducting an architectural comparison between compiled languages (C, C++, Rust) and interpreted languages (Python, JavaScript).
5. **Number Systems & Character Encodings:** Manual conversions across decimal, binary, and hexadecimal radix systems; programmatic validation using Python; developing an interactive conversion utility (`number_converter.py`); and analyzing ASCII versus UTF-8 text encodings.
6. **Version Control with Git & GitHub:** Tracking files, managing staging versus committed snapshots, developing feature branches (`update-about`), creating and merging GitHub Pull Requests (#1), and formulating a comprehensive Git command glossary.
7. **Computer Networking & Web Communication:** Defining network topologies (LAN, MAN, WAN) and foundational protocols; testing connectivity with `ping` and `nslookup`; tracing the 7-step lifecycle of loading a web application from browser to server.
8. **Final System Verification & Quality Audit:** Validating repository structure, auditing privacy compliance (redaction of sensitive IPs/credentials), and finalizing project documentation.

---

## Mission Index
| Mission | Focus Area | Status | Folder Link |
| :--- | :--- | :---: | :--- |
| **Mission 0** | Repository and workspace setup | Completed | [mission-00-setup/](mission-00-setup/README.md) |
| **Mission 1** | Computer fundamentals and IPOS | Completed | [mission-01-computer-basics/](mission-01-computer-basics/README.md) |
| **Mission 2** | Terminal and file management | Completed | [mission-02-terminal/](mission-02-terminal/README.md) |
| **Mission 3** | Operating system, processes and permissions | Completed | [mission-03-operating-system/](mission-03-operating-system/README.md) |
| **Mission 4** | How programs run | Completed | [mission-04-programs/](mission-04-programs/README.md) |
| **Mission 5** | Number systems, Python and text encoding | Completed | [mission-05-numbers-data/](mission-05-numbers-data/README.md) |
| **Mission 6** | Git, GitHub, branches and Pull Requests | Completed | [mission-06-git-github/](mission-06-git-github/README.md) |
| **Mission 7** | Computer networks | Completed | [mission-07-networking/](mission-07-networking/README.md) |
| **Mission 8** | Final review and submission | Completed | [mission-08-final-report/](mission-08-final-report/README.md) |

---

## How to Run the Number Converter Program
The interactive number conversion tool built in **Mission 5** is located in the `mission-05-numbers-data/` folder.

### Step-by-Step Instructions:
1. Open your Terminal.
2. Navigate to the mission directory:
   ```bash
   cd mission-05-numbers-data
   ```
3. Run the script using Python 3:
   ```bash
   python3 number_converter.py
   ```
4. Enter any positive decimal integer when prompted (for example: `13`, `25`, `42`, or `255`).
5. The application will output both the formatted binary representation (prefixed with `0b`) and the hexadecimal representation (prefixed with `0x`), along with the raw digit strings.

---

## My Learning
Throughout this independent assignment, key theoretical computer science concepts were reinforced through direct hands-on practice:
1. **The IPOS Cycle and System Layers:** Experiencing how hardware switches and keyboard interrupts cascade through the OS kernel, memory registers, and storage blocks highlighted the deep synergy between hardware and software.
2. **Command-Line Discipline and Safety:** Operating in the shell emphasized precision—understanding stream redirection (`>` vs `>>`), piping data between programs (`|`), and auditing file permissions to maintain secure filesystems.
3. **Data Representation at the Hardware Level:** Converting values between decimal, binary, and hexadecimal demystified how microprocessors process and store numbers and characters strictly as patterns of binary bits.
4. **Collaborative Version Control:** Branching, opening Pull Requests, and resolving changes modeled industry-standard professional software development workflows.

---

## Mission Workflow & Integrity
- **Sequential Execution:** Every mission was completed in chronological order, fully documented, committed with a descriptive message, and pushed to GitHub before starting the subsequent mission.
- **Privacy Compliance:** In accordance with assignment rules, all personal identification (usernames, local network IP addresses, and authentication tokens) has been strictly redacted (`[redacted]`) from all evidence logs and documentation.
