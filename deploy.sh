#!/bin/bash
# Deployment helper script
# Usage: ./deploy.sh [username] [repo-name]

set -e  # Exit on error

echo "🚀 ML Learning Platform - Deployment Helper"
echo ""

# Get GitHub username
if [ -z "$1" ]; then
    read -p "Enter your GitHub username: " USERNAME
else
    USERNAME=$1
fi

# Get repository name
if [ -z "$2" ]; then
    read -p "Enter repository name [ml-learning-platform]: " REPO
    REPO=${REPO:-ml-learning-platform}
else
    REPO=$2
fi

REPO_URL="https://github.com/$USERNAME/$REPO"

echo ""
echo "📋 Deployment Configuration:"
echo "  Username: $USERNAME"
echo "  Repository: $REPO"
echo "  URL: $REPO_URL"
echo ""

# Step 1: Check if git remote is set
echo "🔍 Checking git configuration..."
if git remote get-url origin &> /dev/null; then
    echo "✓ Remote already configured"
else
    echo "⚠️  No remote configured"
    echo ""
    echo "To set up remote, run:"
    echo "  git remote add origin $REPO_URL.git"
    echo ""
    read -p "Set up remote now? (y/n): " SETUP_REMOTE
    if [ "$SETUP_REMOTE" = "y" ]; then
        git remote add origin "$REPO_URL.git"
        echo "✓ Remote added"
    fi
fi

# Step 2: Check for uncommitted changes
echo ""
echo "📦 Checking for uncommitted changes..."
if [ -n "$(git status --porcelain)" ]; then
    echo "⚠️  You have uncommitted changes"
    git status --short
    echo ""
    read -p "Commit changes? (y/n): " COMMIT
    if [ "$COMMIT" = "y" ]; then
        read -p "Enter commit message: " MSG
        git add -A
        git commit -m "${MSG:-Deploy setup updates}"
        echo "✓ Changes committed"
    fi
else
    echo "✓ No uncommitted changes"
fi

# Step 3: Push to GitHub
echo ""
echo "⬆️  Pushing to GitHub..."
if git push origin main 2>/dev/null; then
    echo "✓ Push successful"
else
    echo "⚠️  Push failed or rejected"
    echo "Attempting to set upstream and push..."
    git push -u origin main
fi

# Step 4: Instructions for GitHub Pages
echo ""
echo "🌐 Next Steps:"
echo ""
echo "1. Go to: $REPO_URL"
echo "2. Click 'Settings' tab"
echo "3. Scroll to 'Pages' in left sidebar"
echo "4. Under 'Source', select 'Deploy from a branch'"
echo "5. Select branch: 'gh-pages' and folder '/' (root)"
echo "6. Click 'Save'"
echo ""
echo "⏳ Wait 2-3 minutes for deployment..."
echo ""
echo "🎉 Your site will be at:"
echo "   https://$USERNAME.github.io/$REPO"
echo ""
echo "📚 Additional Commands:"
echo "  - Check status: git status"
echo "  - View commits: git log --oneline"
echo "  - Build locally: jupyter-book build book/"
echo ""
echo "🔧 Troubleshooting:"
echo "  - If deployment fails, check Actions tab on GitHub"
echo "  - Ensure repository is public (required for free GitHub Pages)"
echo "  - Verify GitHub Actions is enabled in repository settings"
echo ""
echo "✨ Happy teaching!"