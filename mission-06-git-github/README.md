# Mission 6 — Git and GitHub

## 1. Task / objective
The objective of Mission 6 is to master version control fundamentals using Git and GitHub. This includes understanding the lifecycle of staged versus committed changes, creating and isolating feature work in a dedicated branch (`update-about`), opening a Pull Request (PR) on GitHub, merging the changes into `main`, synchronizing local repositories with remote tracking branches, and constructing a comprehensive Git command glossary.

## 2. Work completed
- Explored status inspection, individual file staging, and commit history tracing.
- Created and branched out to `update-about` using `git switch -c update-about`.
- Modified the project root `README.md` to add a new reflective section titled **"My Learning"**.
- Staged and committed the changes on `update-about` and published the branch to GitHub.
- Created Pull Request **#1** on GitHub targeting `main`.
- Reviewed and merged Pull Request #1 into `main`, then synchronized the updated `main` branch locally.
- Formulated the comprehensive Git command glossary.
- Documented findings in `mission-06-git-github/README.md`.

---

## 3. Commands / tools used
| Tool / Command | Purpose | Output / Observation |
| :--- | :--- | :--- |
| `git status` | Inspect current branch state, untracked files, and staged changes | Displayed modified files and branch tracking info. |
| `git add <file>` | Move changes from working directory to the Git staging index | Staged `README.md` for the upcoming commit. |
| `git commit -m "<msg>"` | Record staged snapshot permanently into repository history with a message | Created commit with unique SHA-1 hash. |
| `git log --oneline` | View chronological list of recent commit snapshots | Displayed commit hashes and concise messages. |
| `git switch -c <branch>` | Create a new isolated branch and switch active working tree to it | Created and switched to `update-about`. |
| `git push -u origin <branch>` | Push local branch commits to the remote GitHub repository and set tracking | Published `update-about` to remote GitHub. |
| `gh pr create` | Open an interactive GitHub Pull Request from the CLI | Opened PR #1: `Add My Learning section to root README`. |
| `gh pr merge --merge` | Merge the pull request into the target branch (`main`) on GitHub | PR #1 successfully merged into `main`. |
| `git pull origin main` | Fetch and merge remote changes into current local branch | Fast-forwarded local `main` with merged changes. |

---

## 4. My understanding

### Task 6.1 — Understand the basic Git workflow
| Git Operation | What it does in your own words |
| :--- | :--- |
| **Check repository status (`git status`)** | Audits the current state of the working directory and staging area, identifying untracked files, modified files, and staged changes ready to be committed. |
| **Stage selected changes (`git add`)** | Selectively chooses and prepares specific file modifications to be bundled together into the next upcoming commit snapshot. |
| **Create a commit (`git commit`)** | Permanently records the staged snapshot into the repository history with an author timestamp and a descriptive explanatory message. |
| **View commit history (`git log`)** | Displays the linear or branched timeline of prior commits, allowing developers to review who changed what and when. |

#### Difference Between Staging and Committing:
- **Staging (`git add`)**: Acts as a preparation buffer / drafting table. It allows you to select exactly which changes, lines, or files should be included in the next snapshot. Staging does not permanently save history; files can still be unstaged or modified.
- **Committing (`git commit`)**: Takes an immutable, cryptographic snapshot of everything currently in the staging index and saves it permanently to the repository's database. Once committed, the milestone is recorded with a unique commit hash and can always be retrieved or referenced.

---

### Task 6.2 & 6.3 — Branches and Pull Requests
- **What is a branch?**
  A branch in Git is an independent, lightweight pointer to a specific commit line. Branching allows developers to diverge from the main codebase to experiment, build features, or fix bugs in complete isolation without risking instability on the production `main` branch.
- **What is a Pull Request (PR)?**
  A Pull Request is a collaborative review mechanism hosted on platforms like GitHub. It formally notifies team members that feature work on a branch is complete and ready to be audited, tested, discussed, and reviewed before being merged into the target base branch (`main`).
- **Why are they useful when people work on the same project?**
  Branches prevent developers from stepping on each other's toes or introducing breaking code into the primary production branch. Pull Requests foster peer review, code quality discussions, automated CI/CD validation tests, and clear audit histories before code is merged.

#### Pull Request Activity Evidence:
- **PR Number:** #1
- **PR Title:** `Add My Learning section to root README`
- **Source Branch:** `update-about`
- **Target Base Branch:** `main`
- **Status:** Merged into `main` (commit `403d6d0`)
- **Direct GitHub PR Link:** [https://github.com/akshitsharma98971-commits/digital-detective-2402608002/pull/1](https://github.com/akshitsharma98971-commits/digital-detective-2402608002/pull/1)

---

### Task 6.4 — Git command glossary
| Git Operation | One-Line Explanation in My Own Words |
| :--- | :--- |
| **Initialise a repository (`git init`)** | Sets up a new, empty Git version-tracking repository inside the current project folder. |
| **Check status (`git status`)** | Shows which files are modified, staged, untracked, or unchanged relative to the latest commit. |
| **Stage changes (`git add`)** | Adds working directory file modifications to the staging index for the next commit. |
| **Commit changes (`git commit`)** | Captures the staged changes as a permanent, timestamped snapshot in repository history. |
| **View history (`git log`)** | Lists the chronological log of all historical commits with their authors, dates, and messages. |
| **Create or list branches (`git branch`)** | Displays existing branches or creates a new pointer without immediately switching to it. |
| **Switch branches (`git switch` / `git checkout`)** | Changes the active working context to another specified branch, updating files to that branch state. |
| **Publish changes (`git push`)** | Transmits local commits and branch updates to the remote GitHub server. |
| **Retrieve remote changes (`git pull` / `git fetch`)** | Downloads and integrates recent commits from the remote repository into the local working branch. |

---

## 5. Difficulties faced
- Ensuring remote tracking branches and local branches remain synchronized after merging a Pull Request on GitHub.

## 6. How I resolved them
- Used `git pull origin main` to fast-forward local `main` immediately following the remote GitHub merge of PR #1, and pruned the deleted remote branch.

## 7. Evidence / files
- Pull Request #1: [https://github.com/akshitsharma98971-commits/digital-detective-2402608002/pull/1](https://github.com/akshitsharma98971-commits/digital-detective-2402608002/pull/1)
- Updated root file: `README.md` (containing "My Learning" section)
- Documentation: `mission-06-git-github/README.md`

## 8. Commit details
- **Commit Message:** `Complete Git and GitHub collaboration mission`
- **Pushed to GitHub:** Yes (Branch: `main`)
