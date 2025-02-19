import os
import subprocess

def git_push():
    repo_path = os.getcwd()  # Get current directory (assuming it's the repo)
    os.chdir(repo_path)  # Change to repo directory
    
    try:
        # Add all new/modified files
        subprocess.run(["git", "add", "--all"], check=True)
        
        # Commit changes
        commit_message = "Auto-update: Added new LeetCode solutions"
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        
        # Push to GitHub
        subprocess.run(["git", "push", "origin", "main"], check=True)
        
        print("✅ Successfully pushed to GitHub!")
    except subprocess.CalledProcessError as e:
        print("❌ Error during git operation:", e)

if __name__ == "__main__":
    git_push()
