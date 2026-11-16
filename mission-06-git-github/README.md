# Mission 6 - Git and GitHub

## 1. Task / objective
The objective of this mission was to understand how version control works using Git and GitHub, practice the basic Git workflow (status, add, commit, log), create a feature branch, open and merge a Pull Request on GitHub, and write a glossary of Git commands.

## 2. Work completed
I practiced checking repository status with git status and staging changes with git add.
I learned how commits save snapshots of work with git commit.
I inspected past commit history using git log --oneline.
I created a separate branch named update-about using git switch -c update-about.
In that branch, I updated the root README.md with a section called My Learning.
I committed and pushed the new branch to GitHub.
On GitHub, I created Pull Request #1 from update-about into main, reviewed the changes, and merged it into main.
I pulled the merged changes back onto my local machine so both local and remote are in sync.
I wrote a one-line glossary for common Git operations.

## 3. Commands / tools used
git status: shows the state of the working directory and staging area.
git add: stages modified files so they can be included in the next commit.
git commit: records staged changes into the local repository history with a message.
git log: displays the commit history showing previous saved versions.
git switch -c update-about: creates a new branch named update-about and switches to it.
git push -u origin update-about: uploads the new branch to GitHub.
git switch main: switches active branch back to main.
git pull origin main: fetches and merges the latest commits from GitHub to the local computer.

## 4. My understanding

Task 6.1 - Understand the basic Git workflow

Git operations:
1. Check repository status (git status):
What it does: Checks which files have been modified, which files are untracked, and which changes are staged ready to be saved.

2. Stage selected changes (git add):
What it does: Tells Git to stage specific files or changes into the staging area (index) so they will be part of the upcoming commit.

3. Create a commit (git commit -m):
What it does: Takes the staged changes and permanently saves a snapshot of the project with a message explaining what changed.

4. View commit history (git log):
What it does: Shows a chronological list of commits previously made in the repository, along with their commit IDs and messages.

Difference between staging a change and committing it:
Staging a change (git add) is like putting selected files into a box or preparing them on a desk before sealing them up. You can choose exactly which files go in. Committing (git commit) is like sealing the box, stamping it with a date and message, and permanently storing it in your project history. Staging lets you choose what to save, and committing actually saves it.

Task 6.2 - Create and use a branch
I ran git switch -c update-about to create my new branch.
I added a My Learning section to the root README.md describing the things I have learned so far.
I staged the change with git add README.md, committed it with git commit -m "Add My Learning section to root README", and pushed it with git push -u origin update-about.

Task 6.3 - Create a Pull Request
On GitHub, I created Pull Request #1 comparing branch update-about to main.
After checking the changes, I merged Pull Request #1 into main.
Back in my terminal, I switched to main (git switch main) and ran git pull origin main to sync my computer with GitHub.

Why branches and Pull Requests are useful:
A branch allows a person to work on a new feature or fix in their own separate copy of the code without breaking the working main version of the project.
A Pull Request is a formal request asking project teammates or instructors to review, discuss, and approve changes made in a branch before they get merged into the main project.
Together, branches and Pull Requests let multiple people work on the same software project at the same time without overwriting each other's work or introducing bugs into the main code.

Task 6.4 - Build your Git command glossary
1. Initialise a repository: git init creates a brand new local Git tracking system inside an existing folder.
2. Check status: git status displays modified, untracked, and staged files in the project.
3. Stage changes: git add marks specific modified files to be included in the next commit.
4. Commit changes: git commit saves the staged files permanently into the project history with a description.
5. View history: git log shows the list of past commits with their authors, dates, and messages.
6. Create or list branches: git branch lists current branches or creates a new branch name.
7. Switch branches: git switch moves your working folder between different branches.
8. Publish changes: git push uploads your local commits to a remote hosting platform like GitHub.
9. Retrieve remote changes: git pull downloads and merges updates from GitHub into your local folder.

## 5. Difficulties faced
At first, it was confusing to understand why you need to stage files with git add before committing them, instead of just committing directly. Also, making sure to pull the merged PR changes back to my computer after merging online required careful attention so my local main did not fall behind.

## 6. How I resolved them
Thinking of git add as a preparation step where you pick which files are ready to be saved helped make the idea clear. And running git pull right after switching back to main made sure my computer had the same latest code as GitHub.

## 7. Evidence / files
- Pull Request #1 on GitHub: merged update-about branch into main.
- root README.md: updated with My Learning section.
- mission-06-git-github/README.md: complete Git explanations and glossary.

## 8. Commit details
Commit message: Complete Git and GitHub collaboration mission
Committed and pushed to GitHub repository.
