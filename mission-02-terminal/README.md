# Mission 2 - Become comfortable with the Terminal

## 1. Task / objective
The objective of this mission was to learn how to use the command line terminal, practice basic navigation and file operations safely, understand how command options (flags) and pipes work, and learn what a package manager does.

## 2. Work completed
I practiced essential terminal commands for checking current location, listing files, making directories, creating files, copying, renaming, and reading files.
I created a safe practice folder called terminal-practice inside my repository to avoid messing up any real files.
Inside terminal-practice, I created notes.txt, wrote a first line using echo and redirection, and then added a second line using append (>>) without deleting the first line.
I checked the file with cat to make sure both lines were preserved.
I made a backup copy named notes_backup.txt and then renamed it to notes_archive.txt.
I tested flags like -l, -a, and -h with the ls command to see hidden files and human readable sizes.
I practiced using the pipe symbol (|) to send the output of ls into the head command.
I checked the Homebrew package manager on my Mac and explained why package managers are helpful.
I saved safe terminal output into evidence/mission-02-terminal-log.txt.

## 3. Commands / tools used
pwd: shows the full path of the current working directory.
ls: lists files and folders in the current directory.
ls -l: lists files with extra details like permissions, size, and date.
cd: changes the current working directory, and cd .. goes up one folder.
mkdir: creates a new folder.
touch: creates a new empty file.
cp: makes a copy of a file.
mv: moves or renames a file.
cat: prints the text contents of a file directly to the terminal screen.
echo: prints text, used with > and >> to write into files.
head: displays the first few lines of text output.
brew --version: checks the version of the Homebrew package manager.

## 4. My understanding

Task 2.1 - Explore basic Terminal operations

1. Current directory display (pwd)
- What it does: Prints the complete path of where you currently are in the file system.
- What I observed: It displayed /Users/akshitsharma/.gemini/antigravity/scratch/digital-detective-2402608002.

2. Directory listing (ls)
- What it does: Shows the names of visible files and folders inside the current folder.
- What I observed: It listed mission-00-setup, mission-01-computer-basics, README.md, etc.

3. Detailed listing (ls -l)
- What it does: Shows files in a long format with file permissions, owner name, byte sizes, and last modified date.
- What I observed: Each item was displayed on its own line with extra permission letters like drwxr-xr-x.

4. Change directory (cd ..)
- What it does: Moves your current location one level up into the parent folder.
- What I observed: When I ran cd .. from digital-detective-2402608002, pwd showed I was back in scratch. Then typing cd digital-detective-2402608002 brought me back inside.

5. Create directory (mkdir)
- What it does: Makes a new directory or folder.
- What I observed: I ran mkdir terminal-practice and a new empty folder was created immediately.

6. Create empty file (touch)
- What it does: Creates a brand new empty file if it does not exist yet.
- What I observed: I ran touch terminal-practice/notes.txt and an empty file was created with 0 bytes.

7. Copy file (cp)
- What it does: Duplicates an existing file into a new file with a new name, keeping the original intact.
- What I observed: I ran cp notes.txt notes_backup.txt and both files existed side by side with identical contents.

8. Move or rename file (mv)
- What it does: Renames a file or moves it to another location without duplicating it.
- What I observed: I ran mv notes_backup.txt notes_archive.txt. The backup file was renamed, and the old name was no longer there.

9. Display file contents (cat)
- What it does: Reads and outputs the entire content of a file onto the terminal screen.
- What I observed: Running cat notes.txt printed out the lines of text I had typed inside it.

Task 2.2 - Practise file changes safely
In the terminal-practice folder, I ran:
echo "Line 1: Learning the terminal" > notes.txt
echo "Line 2: Appending a second line" >> notes.txt
cat notes.txt

Questions answered:
1. What is the difference between replacing a file's contents and adding text to the end?
Using a single greater-than sign (>) replaces the entire content of the file from scratch, so whatever was inside before gets erased. Using a double greater-than sign (>>) appends or adds the new line to the very end of the file, preserving everything that was already written.

2. What is the difference between copying a file and moving a file?
Copying creates a second duplicate file, leaving the original file completely untouched in its place. Moving transfers the file to a new place or gives it a new name, so only one file exists when it finishes.

3. What information does the current-directory display provide?
The pwd command shows the exact full path from the root of the computer storage down to the specific folder you are working in right now. This keeps you from accidentally creating or deleting files in the wrong location.

4. Why is a directory-listing operation useful?
The ls command lets you see what files and folders are present in your current folder without opening a graphical window. It helps you check if a file was created properly, verify names before typing commands, and avoid making mistakes.

Task 2.3 - Understand flags and pipes
A flag is an extra letter or word added to a command to change how it works.
Comparing normal ls with ls -la:
- Normal ls only shows visible file names in columns.
- The -l flag shows a detailed long listing with permissions, owner, size, and date.
- The -a flag shows all files, including hidden files that start with a period like .git.
- Adding -h (like in ls -lah) makes file sizes easy to read for humans, showing sizes in KB, MB, or GB instead of raw byte counts.

Pipes:
Command used: ls -la | head -n 5
The vertical bar (|) is called a pipe. It takes the output generated by the command on the left side (ls -la) and feeds it directly as the input to the command on the right side (head -n 5).
The left side generates the full list of files and folders, and the right side takes that stream and prints only the top 5 lines on the screen.

Task 2.4 - Understand package managers
A package manager is a tool that helps search for, install, upgrade, and remove software programs and developer tools from the command line. It also automatically downloads any other helper libraries (dependencies) that the software needs to run properly.
On macOS, Homebrew is the most popular package manager. Running brew --version showed version 4.4.15. Package managers are very useful because they save time, prevent broken installations, and let you update all your developer tools with one simple command.

## 5. Difficulties faced
At first, I accidentally used a single greater-than sign (>) instead of the double one (>>), which wiped out my first line in notes.txt. Also, remembering the difference between flags like -l, -a, and -h took a little bit of practice.

## 6. How I resolved them
To fix the wiped file, I simply typed the first line again using echo with >, and then carefully used >> for the second line. Running cat right after showed both lines clearly. I also tested the flags one by one to see exactly what each flag added to the output.

## 7. Evidence / files
- terminal-practice/notes.txt: practice file with two appended lines.
- terminal-practice/notes_archive.txt: renamed backup copy of notes.txt.
- evidence/mission-02-terminal-log.txt: terminal session log showing the executed commands.

## 8. Commit details
Commit message: Complete Terminal and file management mission
Committed changes to git repository and pushed to GitHub.
