#!/bin/bash
# Git auto-commit script for ML Learning Platform
# Automatically commits progress to Git repository

# Configuration
REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
COMMIT_MESSAGE_PREFIX="[Auto-Commit]"

# Change to repository directory
cd "$REPO_DIR"

# Check if this is a git repository
if [ ! -d ".git" ]; then
    echo "Error: Not a git repository"
    exit 1
fi

# Add progress files
git add logs/
git add data/processed/
git add exports/

# Check if there are changes to commit
if git diff --cached --quiet; then
    echo "No changes to commit"
    exit 0
fi

# Create commit message with timestamp
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')
COMMIT_MESSAGE="$COMMIT_MESSAGE_PREFIX Learning progress update - $TIMESTAMP"

# Commit
git commit -m "$COMMIT_MESSAGE"

echo "✓ Committed learning progress at $TIMESTAMP"

# Optional: Push to remote if configured
# Uncomment the following line if you want to auto-push
# git push origin main