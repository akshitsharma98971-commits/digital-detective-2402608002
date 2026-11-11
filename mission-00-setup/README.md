# Mission 0 — Create your GitHub workspace

## 1. Task / objective
The objective of Mission 0 is to initialize a clean, organized GitHub repository and project folder structure for the entire "Digital Detective" assignment. This includes verifying local development tools (Python 3 and Git), structuring directories for each upcoming mission, creating placeholder README files, and establishing the initial remote repository on GitHub.

## 2. Work completed
- Decided on the repository name matching the assignment standard: `digital-detective-2402608002` (using the USN suffix).
- Verified the local installations of Python 3 and Git.
- Created the local project root folder and initialized a Git version-controlled repository on branch `main`.
- Created dedicated directories for Missions 0 through 8 and an `evidence/` directory:
  - `mission-00-setup/`
  - `mission-01-computer-basics/`
  - `mission-02-terminal/`
  - `mission-03-operating-system/`
  - `mission-04-programs/`
  - `mission-05-numbers-data/`
  - `mission-06-git-github/`
  - `mission-07-networking/`
  - `mission-08-final-report/`
  - `evidence/`
- Created standard `README.md` markdown files inside every mission directory and configured the root `README.md`.
- Connected the local repository to GitHub at `https://github.com/akshitsharma98971-commits/digital-detective-2402608002` and published the workspace.

## 3. Commands / tools used
| Tool / Command | Purpose | Output / Observation |
| :--- | :--- | :--- |
| `python3 --version` | Verify the Python 3 interpreter installation | `Python 3.9.6` |
| `git --version` | Verify the Git version control system installation | `git version 2.55.0` |
| `mkdir <folder>` | Create directories for each mission and evidence | Directory structure generated |
| `touch <file>` | Create empty markdown documents in mission directories | Files created |
| `git init` | Initialize a new Git tracking repository | Initialized empty Git repository |
| `git branch -M main` | Set the primary working branch to `main` | Default branch set to `main` |
| `git remote add origin <url>` | Link local repository to GitHub remote origin | Remote origin configured |
| `git push -u origin main` | Publish local commits and branches to GitHub | Successfully pushed to GitHub |

## 4. My understanding
- **What is a Git repository?** A Git repository is a digital storage space managed by Git that tracks every change, snapshot, and version of files across time. It allows developers to work safely, inspect historical revisions, collaborate across distributed branches, and revert errors without losing progress.
- **Why organize folders by mission?** Modular mission-based folder structure ensures clean separation of concerns. Each topic (e.g., networking, operating systems, binary representations) has self-contained documentation, code, and evidence. This keeps the project easy to navigate, auditable, and modular for iterative evaluation.

## 5. Difficulties faced
- Initially, GitHub remote default branch naming differed between `main` and remote initialization presets, requiring alignment to ensure the assignment's pull request workflow operates smoothly against `main`.

## 6. How I resolved them
- Used `git branch -M main` to guarantee the local primary branch is `main`, and set remote default branch via GitHub CLI `gh repo edit --default-branch main`.

## 7. Evidence / files
- Root index file: `README.md`
- Mission setup file: `mission-00-setup/README.md`
- Folders: `mission-00-setup/` through `mission-08-final-report/` and `evidence/`

## 8. Commit details
- **Commit Message:** `Set up Digital Detective mission structure`
- **Pushed to GitHub:** Yes (Branch: `main`)
