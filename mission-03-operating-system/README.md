# Mission 3 - Understand the operating system

## 1. Task / objective
The objective of this mission was to explore what an operating system does, inspect my operating system environment and storage from the terminal, understand what processes and PIDs are, learn the difference between absolute and relative paths, understand file permissions (read, write, execute), and explain key responsibilities of the operating system.

## 2. Work completed
I used terminal commands to check my operating system name, kernel version, current user account, and available hard drive space.
I inspected running processes using ps and top, noted process IDs (PIDs), and explained what a process is.
I practiced navigating between parent and child directories to understand absolute and relative paths.
I inspected the file permission string on my notes.txt file using ls -l and identified what r, w, and x stand for.
I wrote explanations and simple everyday examples for the six main operating system responsibilities.

## 3. Commands / tools used
sw_vers: displays macOS product name and version number.
uname -a: displays the operating system kernel name, machine architecture, and release date.
whoami: prints the active username of the current user account.
df -h: displays free and used disk storage space in human-readable gigabyte format.
ps aux: lists currently running processes on the computer along with their PID, CPU usage, and memory usage.
ls -l: shows detailed file information including permission flags.

## 4. My understanding

Task 3.1 - Explore your operating system

1. Operating system / system details
- What it tells you: The exact name, version, and architecture of the operating system and kernel running on the machine.
- My observation: macOS version 15.0.1 (Darwin Kernel version 24.0.0, architecture arm64).

2. Current account identity
- What it tells you: Which user account is currently logged into the computer session.
- My observation: [redacted] (non-root standard user account).

3. Available and used storage
- What it tells you: How much total disk space is mounted, how much space has been used by files and system software, and how much free capacity remains.
- My observation: System disk capacity around 460G, with used space of 350G and available space around 110G.

4. System activity snapshot
- What it tells you: A live view of currently running tasks, showing CPU usage percentage, memory usage, and background services.
- My observation: Over 300 total processes running, with low idle CPU load and moderate memory usage.

Task 3.2 - Understand processes
1. What is a process?
A process is a program or application that is currently loaded into memory and being executed by the computer processor. Even when you are not actively interacting with an application, it can run in the background as a process.

2. What does the PID column represent?
PID stands for Process Identifier. It is a unique number assigned by the operating system to each running program when it starts. The OS uses this number to track, manage, give resources to, or stop that specific process.

3. Give two examples of processes that may be running on your computer:
- Google Chrome (or another web browser application running in the foreground to view websites).
- launchd (a background system process on macOS that starts and manages system services and daemons).

Task 3.3 - Understand paths and permissions

Absolute path vs Relative path:
An absolute path specifies the full location of a file or folder starting all the way from the root directory of the computer (symbolized by /). It works from anywhere on the system.
- Example from my assignment: /Users/akshitsharma/.gemini/antigravity/scratch/digital-detective-2402608002/terminal-practice/notes.txt

A relative path specifies the location of a file or folder relative to the current working directory where you are standing right now.
- Example from my assignment: If I am standing inside digital-detective-2402608002, the relative path to notes.txt is terminal-practice/notes.txt.

File permissions:
When running ls -l on notes.txt, I saw the permission string -rw-r--r--.
- r (Read): Allows the contents of the file to be opened and viewed.
- w (Write): Allows the file contents to be modified, edited, or saved.
- x (Execute): Allows the file to be executed as a program or script. For directories, it allows entering and browsing inside the folder.

For my practice file notes.txt:
The owner permissions are rw-, which means the owner (me) can read and write to the file, but cannot execute it as a program. The group and others have r--, meaning they can only read the file.

Task 3.4 - Explain operating-system responsibilities

1. Process management
- Explanation: The OS schedules and controls when programs run on the CPU so that multiple programs can share the processor without crashing into each other.
- Example: Letting you listen to music in Spotify while typing an assignment in a text editor at the same time.

2. Memory management
- Explanation: The OS allocates pieces of RAM memory to each running program when it needs data, and frees up that memory when the program closes.
- Example: Allocating RAM to open 10 tabs in a browser and releasing that RAM when tabs are closed.

3. Device management
- Explanation: The OS communicates with physical hardware devices using software drivers so applications do not have to know the low-level electronics of every gadget.
- Example: Sending a document to a USB printer through the printer driver when you click print.

4. File management
- Explanation: The OS organizes, creates, reads, and deletes files and folders on your storage drive, keeping track of where files are located.
- Example: Storing notes.txt inside the terminal-practice folder on the SSD.

5. User interface / shell
- Explanation: The OS provides a visual desktop or a command-line terminal shell so humans can easily give instructions to the computer.
- Example: Using Terminal (zsh) or the macOS Finder window to click or type commands to launch apps.

6. Security and permissions
- Explanation: The OS protects files and system settings so that unauthorized users or programs cannot alter or delete important data.
- Example: Requiring a password or Touch ID before installing new software or accessing protected system folders.

## 5. Difficulties faced
Understanding the permission string like -rw-r--r-- felt confusing at first glance because it looks like a bunch of random dashes and letters. Also understanding how relative paths change based on where you are currently standing took a few tries.

## 6. How I resolved them
I broke down the 9 permission characters into three groups of three letters: owner, group, and others. Each group has r for read, w for write, and x for execute. Seeing it broken into those three triplets made it very simple to understand.

## 7. Evidence / files
- mission-03-operating-system/README.md: contains system notes, process explanations, path examples, and OS responsibilities.

## 8. Commit details
Commit message: Document operating system and file management
Changes staged, committed, and pushed to GitHub.
