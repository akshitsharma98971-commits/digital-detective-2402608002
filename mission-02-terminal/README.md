# Mission 2 — Become comfortable with the Terminal

## 1. Task / objective
The objective of Mission 2 is to gain proficiency with the command-line interface (CLI), perform safe file and directory inspection, create and manipulate files without data loss, understand how flags and pipes modify command behavior, and explain the fundamental role of software package managers.

## 2. Work completed
- Explored essential terminal commands (`pwd`, `ls`, `cd`, `mkdir`, `touch`, `cp`, `mv`, `cat`).
- Created a safe isolated sandbox directory `terminal-practice/` inside the assignment repository.
- Practiced safe file creation, appending content without overwriting existing data, copying files, and renaming backup files.
- Analyzed command-line options (`-l`, `-a`, `-h`) and Unix pipeline chaining (`|`).
- Inspected the local package manager (Homebrew) and evaluated its package tracking.
- Captured privacy-safe command logs in `evidence/mission-02-terminal-log.txt`.

---

## 3. Commands / tools used
| Operation / Command Name | What it does | What I observed |
| :--- | :--- | :--- |
| **Current-directory display (`pwd`)** | Prints the full absolute pathname of the current working directory to standard output. | Displayed the exact directory path from the root down to `digital-detective-2402608002`. |
| **Directory listing (`ls`)** | Lists non-hidden file and folder names in the current working directory. | Displayed mission folders and files arranged across terminal columns. |
| **Detailed listing (`ls -l`)** | Lists directory contents with long metadata: permissions, link count, owner, group, file size, and modification timestamp. | Showed detailed permission strings (e.g. `drwxr-xr-x`, `-rw-r--r--`), file size in bytes, and dates. |
| **Change directory (`cd ..`)** | Moves the current shell context up one directory level into the parent directory. | The working directory path changed to the parent folder; running `pwd` confirmed the new location. |
| **Create directory (`mkdir`)** | Generates a new directory folder at the specified target path. | Created the practice workspace folder `terminal-practice/`. |
| **Create empty file (`touch`)** | Creates an empty file if it does not exist, or updates access and modification timestamps if it exists. | Generated an empty file `original.txt` with an initial size of 0 bytes. |
| **Copy file (`cp`)** | Duplicates a source file to a new target path while preserving the original source file. | Created `backup_original.txt` with identical contents while leaving `original.txt` intact. |
| **Move / rename file (`mv`)** | Moves a file to a new path or renames it within the file system without copying contents. | Renamed `backup_original.txt` to `archived_original.txt`; the previous filename ceased to exist. |
| **Display file contents (`cat`)** | Concatenates and prints the contents of text files to standard output. | Printed all lines of `original.txt` to the terminal terminal output cleanly. |

---

## 4. My understanding

### Task 2.2 — Practise file changes safely
Inside `terminal-practice/`:
1. Generated `original.txt` and populated it using `echo "Line 1: Exploring Terminal operations." > original.txt`.
2. Appended a second line using `echo "Line 2: Successfully appending data without overwriting." >> original.txt`.
3. Verified both lines were retained using `cat original.txt`.
4. Duplicated with `cp original.txt backup_original.txt` and renamed using `mv backup_original.txt archived_original.txt`.

#### Core Conceptual Questions Answered:
- **What is the difference between replacing a file's contents and adding text to the end?**
  Using the single redirect operator `>` truncates (clears) the entire target file before writing new data, completely overwriting whatever existed previously. In contrast, using the double redirect operator `>>` opens the file in append mode, preserving all existing contents and appending the new stream strictly to the end of the file.
- **What is the difference between copying a file and moving a file?**
  Copying (`cp`) creates a distinct duplicate with its own separate storage blocks and new inode; modifying the copy has no effect on the original. Moving (`mv`) either relocates a file pointer or changes its directory entry name within the filesystem without duplicating disk blocks; the file under the old name disappears.
- **What information does the current-directory display provide?**
  The `pwd` (print working directory) command gives unambiguous geographical orientation within the hierarchical file system tree. It reveals the exact absolute path from the root directory (`/`) to the active folder, preventing accidental operations in incorrect directories.
- **Why is a directory-listing operation useful?**
  A directory listing (`ls`) allows the user to inspect what files and subdirectories exist in a directory, verify recent file creations or modifications, check spelling, and examine attributes such as permissions, ownership, and byte sizes.

---

### Task 2.3 — Understand flags and pipes
- **Flags and Options (`ls` vs `ls -lah`):**
  - Standard `ls` outputs only non-hidden file and folder names in compact columnar text.
  - Adding `-l` (long format) exposes metadata columns: Unix file mode/permissions, hard link count, owner, group, file size, and timestamp.
  - Adding `-a` (all) exposes hidden dotfiles (such as `.`, `..`, and `.git/`) that are normally suppressed.
  - Adding `-h` (human-readable) converts raw byte values into human-readable units such as `2.6K`, `480B`, or `12M`.
- **Pipes (`|`):**
  - Command tested: `ls -la | head -n 5`
  - **What the pipe does:** The pipe operator `|` acts as an inter-process communication conduit. It connects the standard output (`stdout`) stream of the command on its left directly to the standard input (`stdin`) stream of the command on its right.
  - **Contribution of each side:** The left command (`ls -la`) generates a complete directory listing. The right command (`head -n 5`) receives that stream and filters it, passing only the first 5 lines to the terminal screen, discarding the rest.

---

### Task 2.4 — Understand package managers
- **Homebrew on macOS:**
  Checked with `brew --version`: **Homebrew 7.0.10**. Listed installed packages (`brew list --formula`) including utilities like `ca-certificates`, `cairo`, `dav1d`, `ffmpeg`, and `freetype`.
- **Why Package Managers are Useful:**
  Package managers automate the discovery, installation, configuration, dependency resolution, updating, and removal of software libraries and command-line tools from unified repositories. Instead of manually searching websites, compiling C/C++ source code, and troubleshooting conflicting dependencies, a package manager resolves dependency graphs automatically, installs verified binaries into standard paths, and ensures system cleanliness.

---

## 5. Difficulties faced
- Remembering whether single `>` or double `>>` is used for appending without erasing file contents.

## 6. How I resolved them
- Tested both operators in the `terminal-practice` directory with dummy files, verifying with `cat` that `>` overwrites whereas `>>` appends cleanly.

## 7. Evidence / files
- `terminal-practice/original.txt`
- `terminal-practice/archived_original.txt`
- `evidence/mission-02-terminal-log.txt`

## 8. Commit details
- **Commit Message:** `Complete Terminal and file management mission`
- **Pushed to GitHub:** Yes (Branch: `main`)
