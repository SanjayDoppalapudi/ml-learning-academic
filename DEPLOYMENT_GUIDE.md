# Deploy to GitHub Pages

This guide will walk you through deploying your ML Learning Platform to GitHub Pages using JupyterBook.

## 📋 Prerequisites

- GitHub account
- Git installed locally
- Your ML Learning Platform code ready

## 🚀 Quick Deploy (5 minutes)

### Step 1: Create GitHub Repository

1. Go to https://github.com/new
2. Repository name: `ml-learning-platform` (or any name you prefer)
3. Make it **Public** (required for free GitHub Pages)
4. **DO NOT** initialize with README (we'll push our own)
5. Click **Create repository**

### Step 2: Push Your Code

```bash
# Navigate to your project
cd ml-learning-academic

# Add the remote repository (replace with your username)
git remote add origin https://github.com/YOUR_USERNAME/ml-learning-platform.git

# Rename branch to main (if not already)
git branch -M main

# Push to GitHub
git push -u origin main
```

### Step 3: Enable GitHub Pages

1. Go to your repository on GitHub
2. Click **Settings** (tab at top)
3. Scroll down to **Pages** section (left sidebar)
4. Under "Source", select **Deploy from a branch**
5. Under "Branch", select **gh-pages** and folder **/(root)**
6. Click **Save**

Wait 2-3 minutes for the site to build...

### Step 4: View Your Site

Your site will be at:
```
https://YOUR_USERNAME.github.io/ml-learning-platform
```

🎉 **Done!** Your ML Learning Platform is now live!

---

## 🔧 Detailed Setup (With Auto-Deployment)

### Option A: Manual Build & Deploy

Build locally and push to gh-pages branch:

```bash
# Install JupyterBook
pip install jupyter-book

# Build the book
jupyter-book build book/

# The built site is in book/_build/html/
# You can manually push this to gh-pages branch
```

### Option B: Auto-Deployment (Recommended)

We'll set up GitHub Actions to automatically build and deploy when you push changes.

#### 1. Create GitHub Actions Workflow

I've already created this file for you: `.github/workflows/deploy.yml`

```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.9'

      - name: Install dependencies
        run: |
          pip install jupyter-book
          pip install -r requirements.txt

      - name: Build JupyterBook
        run: jupyter-book build book/

      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        if: github.ref == 'refs/heads/main'
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: book/_build/html
```

#### 2. Commit and Push

```bash
git add .github/workflows/deploy.yml
git commit -m "Add GitHub Actions for auto-deployment"
git push origin main
```

Now every time you push to main, GitHub Actions will:
1. Build the JupyterBook
2. Deploy to GitHub Pages automatically

---

## 🎨 Customization

### Update Book Configuration

Edit `book/_config.yml`:

```yaml
title: Your Title
author: Your Name
repository:
  url: https://github.com/YOUR_USERNAME/ml-learning-platform
html:
  use_repository_button: true
  use_issues_button: true
```

### Add Your Logo

1. Add a logo image to `book/logo.png`
2. Update `_config.yml`:
   ```yaml
   logo: logo.png
   ```

### Custom Domain (Optional)

1. Add domain to `book/CNAME`:
   ```
   ml-learning.yourdomain.com
   ```
2. Configure DNS with your domain provider
3. Enable HTTPS in GitHub Pages settings

---

## 📝 Content Management

### Adding New Content

1. Create markdown or notebook files in `book/` directory
2. Update `book/_toc.yml` to include new files
3. Commit and push:
   ```bash
   git add .
   git commit -m "Add new content"
   git push origin main
   ```
4. GitHub Actions will auto-deploy!

### File Structure for Web

```
book/
├── _config.yml          # Site configuration
├── _toc.yml            # Navigation structure
├── intro.md            # Homepage
├── module_0/
│   ├── index.md
│   └── *.ipynb or *.md
├── module_1/
│   ├── index.md
│   ├── *.md or *.ipynb
│   └── exercises/
└── appendix/
```

---

## 🔍 Troubleshooting

### Build Fails

Check GitHub Actions logs:
1. Go to repository → Actions tab
2. Click on failed workflow
3. Check error messages

Common issues:
- Missing dependencies → Add to requirements.txt
- Syntax errors in notebooks → Fix locally first
- Large files → Add to .gitignore

### Site Not Updating

1. Check that GitHub Pages source is set to gh-pages branch
2. Wait 2-3 minutes after push
3. Clear browser cache (Ctrl+Shift+R)
4. Check Actions tab for build status

### 404 Errors

- Verify file paths in `_toc.yml`
- Ensure files are committed
- Check case sensitivity (Linux servers are case-sensitive)

---

## 🌟 Features After Deployment

Your deployed site will have:

✅ **Full navigation** - Sidebar with all modules and projects  
✅ **Search functionality** - Search all content  
✅ **Mobile responsive** - Works on phones/tablets  
✅ **Dark mode** - Toggle light/dark theme  
✅ **Binder integration** - Launch interactive notebooks  
✅ **Download buttons** - PDF, Markdown exports  
✅ **Progressive web app** - Can be installed on mobile  

---

## 📊 Monitoring

### View Analytics

1. Go to repository Settings → Pages
2. View traffic data
3. Or add Google Analytics to `_config.yml`:
   ```yaml
   html:
     google_analytics_id: GA_MEASUREMENT_ID
   ```

### Update Frequency

- Manual push → Immediate rebuild
- Scheduled updates → Use GitHub Actions cron

---

## 🚀 Next Steps After Deployment

1. **Test the site** - Click through all pages
2. **Share the URL** - Send to friends/colleagues
3. **Add custom domain** - For professional look
4. **Enable discussions** - For Q&A
5. **Add badges** - Build status, license, etc.

---

## 🆘 Need Help?

- **JupyterBook docs**: https://jupyterbook.org
- **GitHub Pages docs**: https://docs.github.com/pages
- **Common issues**: Check TROUBLESHOOTING.md

---

**Your ML Learning Platform will be accessible worldwide! 🌍**