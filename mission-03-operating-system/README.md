# Mission 3 — Understand the operating system

## 1. Task / objective
The objective of Mission 3 is to investigate the core role and architectural responsibilities of the Operating System (OS). This includes auditing system specifications, user account context, storage utilization, inspecting running processes and Process Identifiers (PIDs), understanding absolute versus relative path navigation, deciphering Unix file permission bits (`r`, `w`, `x`), and detailing the primary responsibilities of modern operating systems.

## 2. Work completed
- Inspected operating system details, active account privileges, disk filesystem capacity, and running process tables using Terminal.
- Explored running process hierarchies and identified foreground and background process behaviors.
- Examined file system paths, establishing the concrete distinction between absolute and relative file paths within the assignment workspace.
- Audited POSIX file permission triples (`rw-r--r--`) for files created in `terminal-practice/`.
- Completed an analysis of the six core responsibilities of modern operating systems.
- Documented findings in `mission-03-operating-system/README.md`.

---

## 3. Commands / tools used
| Command | Purpose | Privacy-Safe Output / Finding |
| :--- | :--- | :--- |
| `sw_vers` & `uname -smr` | Identify operating system name, version build, kernel release, and hardware architecture | `macOS 27.2 (Darwin 27.2.0 arm64)` |
| `whoami` | Report current effective logged-in username | `[redacted_user]` |
| `df -h /` | Display total disk space, utilized blocks, and available storage on the root mount point | Total: `926 GiB`, Used: `13 GiB`, Avail: `763 GiB` (Capacity: `2%`) |
| `ps -eo pid,user,%cpu,%mem,comm` | Snapshot active processes, PIDs, user ownership, resource consumption, and command paths | Identified PID 1 (`launchd`), background system daemons, and user processes |
| `ls -l <file>` | Inspect Unix file mode permission bits and ownership | Owner: `rw-` (Read & Write permissions) |

---

## 4. My understanding

### Task 3.1 — Explore your operating system
| Information explored | What it tells you | Your observation (privacy-safe) |
| :--- | :--- | :--- |
| **Operating system / system details** | Identifies the software distribution, kernel version, and processor architecture on which software runs. | macOS 27.2 running Darwin 27.2.0 on 64-bit ARM architecture (`arm64`). |
| **Current account identity** | Confirms the active user shell session identity and security context for access control permissions. | User: `[redacted_user]` (standard non-root administrator account). |
| **Available and used storage** | Shows overall non-volatile storage partition size, currently occupied disk blocks, and remaining free space. | APFS Container (`/dev/disk3s1s1`), Total: 926 GiB, Used: 13 GiB, Available: 763 GiB. |
| **System activity snapshot** | Reveals live CPU and RAM allocation across currently executing processes and daemon tasks. | Init daemon PID 1 (`/sbin/launchd`) coordinating system services; low steady-state CPU utilization (<1%). |

---

### Task 3.2 — Understand processes
- **What is a process?**
  A process is an active instance of a computer program currently in execution. Unlike passive code sitting on disk storage, a process possesses active state: an address space in RAM, program counters, CPU execution registers, stack/heap structures, and open file descriptors managed by the OS kernel.
- **What does the PID column represent?**
  PID stands for **Process Identifier**. It is a unique positive integer assigned by the operating system kernel to identify and track each active process throughout its lifecycle. The OS uses PIDs to allocate CPU slices, monitor memory, apply permissions, and deliver signals (e.g. `SIGTERM`, `SIGKILL`).
- **Two examples of processes running on the computer:**
  1. `/sbin/launchd` (PID 1): The macOS root initialization process that bootstraps system services, launches background daemons, and manages the user login session.
  2. `Visual Studio Code` / `Terminal` (`zsh`): Foreground interactive application and shell processes responding directly to user commands and input events.

---

### Task 3.3 — Understand paths and permissions
- **Absolute Path vs. Relative Path:**
  - **Absolute Path:** The complete, unambiguous location of a file or directory starting from the root of the file system hierarchy (`/`). It is independent of the current working directory.
    - *Example:* `/Users/[redacted_user]/.gemini/antigravity/scratch/digital-detective-2402608002/terminal-practice/original.txt`
  - **Relative Path:** The location of a file or directory specified relative to the current working directory, often using `.` (current directory) or `..` (parent directory).
    - *Example (from project root):* `terminal-practice/original.txt` or `./mission-03-operating-system/README.md`
- **File Permissions Analysis:**
  Inspected `terminal-practice/original.txt`: `-rw-r--r--`
  - **First character (`-`):** Regular file (directory would be `d`).
  - **Owner permissions (`rw-`):** The file owner has **Read (`r`)** and **Write (`w`)** permissions, but does **not** have **Execute (`x`)** permission.
  - **Group permissions (`r--`):** Group members have Read-only permission.
  - **Others permissions (`r--`):** All other users have Read-only permission.

| Permission Bit | Meaning | Concrete Example |
| :--- | :--- | :--- |
| **`r` — Read** | Allows opening and reading the content of a file; on a directory, allows listing contents with `ls`. | Viewing `README.md` using `cat` or opening a document in an editor. |
| **`w` — Write** | Allows modifying, appending, or deleting a file's contents; on a directory, allows adding or removing files. | Modifying a Python script or saving updates to a log. |
| **`x` — Execute** | Allows running a file as an executable program or script; on a directory, allows traversal (`cd`). | Executing a shell script `./deploy.sh` or traversing into a directory. |

---

### Task 3.4 — Explain operating-system responsibilities

| OS Responsibility | Your Explanation | Example |
| :--- | :--- | :--- |
| **Process management** | Allocates CPU cores and time slices among competing programs using preemptive scheduling; manages process creation, suspension, and termination. | Switching CPU execution rapidly between a web browser, code editor, and music player so all run concurrently without freezing. |
| **Memory management** | Allocates and tracks physical RAM addresses for active programs; isolates process address spaces and implements virtual memory swapping to disk when RAM is full. | Reserving 500 MB of RAM for a Python data process while protecting kernel memory from unauthorized overwrite. |
| **Device management** | Provides a standardized hardware abstraction layer via device drivers to control internal and external peripheral hardware (keyboards, disks, GPUs). | Translating a generic file-save request into specific SATA/NVMe controller protocol commands to write NAND flash cells. |
| **File management** | Manages logical organization, directory trees, file metadata, access permissions, and efficient storage block allocation on persistent media. | Maintaining an APFS / ext4 hierarchical filesystem tree mapping `/Users/...` to physical disk sectors. |
| **User interface / shell** | Provides an interface (Graphical GUI or Command-Line CLI) allowing humans to interact with and control system services. | The macOS Aqua desktop GUI window server or the Terminal interactive Zsh command-line shell. |
| **Security and permissions** | Authenticates user identities, enforces privilege separation, restricts access to sensitive system resources, and protects user data. | Enforcing POSIX file permissions (`chmod`), sandboxing application capabilities, and requiring administrative credentials for system modifications. |

---

## 5. Difficulties faced
- Interpreting process outputs where system daemons run under the `root` user while user apps run under a personal UID.

## 6. How I resolved them
- Reviewed Unix process ownership concepts and verified that child processes inherit permissions unless elevated, confirming security isolation.

## 7. Evidence / files
- Documented findings: `mission-03-operating-system/README.md`
- Permission test file: `terminal-practice/original.txt`

## 8. Commit details
- **Commit Message:** `Document operating system and file management`
- **Pushed to GitHub:** Yes (Branch: `main`)
