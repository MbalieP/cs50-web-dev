# 🛠️ Git Basic Workflow Guide

A concise, commented guide to using Git for daily development tasks.

---

## 📦 Staging Changes

```bash
git add <file>        # Stage a specific file
git add .             # Stage all changes in the current directory (recursive)
git add -A            # Stage all changes across the entire repo (add/delete/update)
✅ Committing Changes
bash
Copy code
git commit -m "message"     # Commit staged changes with a message
git commit -am "message"    # Stage tracked files and commit (skips 'git add')
🔍 Viewing Status and History
bash
Copy code
git status             # Show working tree status
git log                # View detailed commit history
git log --oneline      # Condensed commit history (1 line per commit)
🌿 Branching & Merging
📂 Branch Operations
bash
Copy code
git branch                       # List all local branches
git branch <branch-name>         # Create a new branch
git checkout -b <branch-name>    # Create and switch to new branch
git checkout <branch-name>       # Switch to existing branch
git switch <branch-name>         # Preferred way to switch (newer syntax)
git branch -d <branch-name>      # Delete a local branch
🔀 Merging
bash
Copy code
git merge <branch-name>          # Merge given branch into the current branch
♻️ Undoing Changes
❌ Reset Options (Be Careful)
bash
Copy code
git reset --hard <commit>          # Reset working dir and index (destructive)
git reset --hard origin/<branch>   # Reset to match remote branch state
git reset --soft <commit>          # Move HEAD, keep changes staged
git restore <file>                 # Discard local changes in a file
🛡️ Revert (Safe Alternative)
bash
Copy code
git revert <commit>               # Create a new commit that undoes previous commit
🌐 Remote Operations
🔗 Basic Remote Commands
bash
Copy code
git clone <url>                  # Clone a repository
git push origin <branch>         # Push current branch to remote
git pull origin <branch>         # Fetch and merge changes from remote
git fetch                        # Download changes without merging
🌍 Remote Tracking
bash
Copy code
git remote -v                    # List remotes with URLs
git branch -a                    # Show all branches (local + remote)
⚔️ Conflict Resolution
🧩 Handling Merge Conflicts
When a conflict occurs during a merge:

bash
Copy code
# Edit conflicted files (look for <<<<<<< HEAD markers)
git add <resolved-files>         # Mark conflicts as resolved
git commit                       # Complete the merge
🔙 Aborting Merge/Reset
bash
Copy code
git merge --abort                # Cancel the merge process
git reset --merge                # Alternative way to abort (resets index and working tree)
🚧 Advanced Techniques
📥 Stashing Changes
bash
Copy code
git stash                        # Save working directory changes temporarily
git stash pop                    # Apply and remove most recent stash
git stash list                   # Show list of stashed changes
git stash apply <stash-id>       # Apply a specific stash
🔍 Viewing Differences
bash
Copy code
git diff                         # Show changes not staged
git diff --staged                # Show staged changes
git diff <commit1> <commit2>     # Compare two commits
git diff <branch1> <branch2>     # Compare two branches
🏷️ Tagging
bash
Copy code
git tag <tagname>                        # Create a lightweight tag
git tag -a <tagname> -m "message"       # Create an annotated tag
git push origin <tagname>               # Push tag to remote
🔁 Common Workflows
🌟 Feature Branch Workflow
bash
Copy code
# Start a new feature
git checkout -b feature/new-feature

# Make changes and commit
git add .
git commit -m "Implement new feature"

# Switch to main and update
git checkout main
git pull origin main

# Merge feature branch
git merge feature/new-feature

# Push to remote
git push origin main

# Delete the feature branch locally
git branch -d feature/new-feature
🚨 Emergency Fix Workflow (Hotfix)
bash
Copy code
# Stash current work
git stash

# Create hotfix branch
git checkout -b hotfix/emergency

# Make and commit fix
git add .
git commit -m "Emergency fix"

# Merge fix into main
git checkout main
git merge hotfix/emergency
git push origin main

# Restore previous work
git checkout previous-branch
git stash pop
💡 Pro Tips
Commit Often: Small, atomic commits are easier to manage and debug.

Write Good Messages: Use imperative mood — e.g., “Fix bug” instead of “Fixed bug”.

Pull Before Push: Avoid conflicts by syncing with remote before pushing.

Use .gitignore: Prevent unwanted files (e.g., logs, dependencies) from being tracked.

Review with git diff: Always review your code changes before committing.

⚠️ Danger Zone
Reset and Rebase commands can rewrite history.
Avoid using them on shared branches unless you're absolutely sure.

bash
Copy code
git reset --hard         # ⚠️ Destroys local changes
git rebase -i HEAD~3     # ⚠️ Rewrite commit history
🙌 Final Note
Git is a powerful tool that becomes more intuitive with practice.
Don’t stress about memorizing commands — focus on understanding the concepts.

Happy coding! 🚀






