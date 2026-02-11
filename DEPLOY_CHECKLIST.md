# 🚀 Deployment Checklist

## Pre-Flight Check ✅

Before deploying, verify:
- [ ] You have a GitHub account
- [ ] Git is installed locally
- [ ] You're in the ml-learning-academic directory
- [ ] All your content is committed

---

## Step-by-Step Deployment

### Step 1: Create GitHub Repository (2 minutes)

**Option A: Web Interface**
1. Go to https://github.com/new
2. Repository name: `ml-learning-platform`
3. Description: "Interactive ML learning platform with JupyterBook"
4. Choose **Public** (required for free GitHub Pages)
5. **DO NOT** check "Initialize with README"
6. Click **Create repository**

**Option B: GitHub CLI**
```bash
gh repo create ml-learning-platform --public --description "Interactive ML learning platform"
```

---

### Step 2: Push Code (1 minute)

**Easy way (using our script):**
```bash
./deploy.sh YOUR_GITHUB_USERNAME ml-learning-platform
```

**Manual way:**
```bash
# Add remote
git remote add origin https://github.com/YOUR_GITHUB_USERNAME/ml-learning-platform.git

# Push code
git branch -M main
git push -u origin main
```

**Verify push worked:**
- Go to https://github.com/YOUR_GITHUB_USERNAME/ml-learning-platform
- You should see all your files

---

### Step 3: Enable GitHub Pages (1 minute)

1. Go to your repository on GitHub
2. Click **Settings** tab (top right)
3. In left sidebar, scroll to **Pages**
4. Under "Source", select **Deploy from a branch**
5. Under "Branch", select:
   - Branch: **gh-pages**
   - Folder: **/(root)**
6. Click **Save**

**Alternative: GitHub Actions will create gh-pages automatically**
- Just push to main and wait 2-3 minutes
- The workflow will build and deploy automatically

---

### Step 4: Verify Deployment (2 minutes)

1. Go to **Actions** tab in your repository
2. You should see a workflow running: "Deploy to GitHub Pages"
3. Wait for it to complete (should be green ✅)
4. Go to **Settings** → **Pages**
5. You'll see a green badge saying "Your site is published at:"
6. Click the URL!

**Your URL:**
```
https://YOUR_GITHUB_USERNAME.github.io/ml-learning-platform
```

---

## 🎉 Success Indicators

You've successfully deployed if:
- [ ] GitHub Actions workflow shows green checkmark
- [ ] Settings → Pages shows green "published" badge
- [ ] You can visit the URL and see your content
- [ ] Navigation sidebar shows all modules

---

## 🔄 Making Updates

After initial deployment, updating is automatic:

```bash
# Edit your content
git add .
git commit -m "Update content"
git push origin main
# GitHub Actions automatically rebuilds and deploys!
```

---

## 🆘 Troubleshooting

### Problem: GitHub Actions shows red X (failed)

**Solution:**
1. Click on the failed workflow
2. Check which step failed
3. Common fixes:
   - **Install dependencies failed**: Check requirements.txt
   - **Build failed**: Check for syntax errors in notebooks
   - **Deploy failed**: Check repository permissions

### Problem: Site shows 404

**Solution:**
1. Wait 3-5 minutes (first deployment takes time)
2. Check Settings → Pages source is set to gh-pages
3. Ensure repository is public
4. Check _toc.yml for incorrect file paths

### Problem: Changes not appearing

**Solution:**
1. Clear browser cache (Ctrl+Shift+R)
2. Check Actions tab for new build
3. Verify you pushed to main branch

### Problem: Images not loading

**Solution:**
1. Use relative paths: `./images/pic.png`
2. Ensure images are committed to repository
3. Check case sensitivity (Pic.png ≠ pic.png)

---

## 🎨 Customization (Optional)

### Add Custom Domain

1. Buy domain from Namecheap/GoDaddy/etc
2. Add file `book/CNAME` with your domain:
   ```
   ml-learning.yourdomain.com
   ```
3. Configure DNS:
   - Type: CNAME
   - Name: ml-learning
   - Value: YOUR_USERNAME.github.io
4. Enable HTTPS in GitHub Pages settings

### Add Google Analytics

Edit `book/_config.yml`:
```yaml
html:
  google_analytics_id: G-XXXXXXXXXX
```

### Change Theme

Edit `book/_config.yml`:
```yaml
sphinx:
  config:
    html_theme: sphinx_book_theme  # or sphinx_rtd_theme
```

---

## 📊 Post-Deployment Checklist

Test your deployed site:

- [ ] Homepage loads correctly
- [ ] Module 0 content displays
- [ ] Module 1 projects are accessible
- [ ] Exercise sets are readable
- [ ] Navigation works on mobile
- [ ] Search function works
- [ ] Dark mode toggle works
- [ ] Links to GitHub work

---

## 🎯 Next Steps After Deployment

1. **Test thoroughly** - Click every link
2. **Share the URL** - Post on social media, forums
3. **Add to resume** - Showcases your ML knowledge
4. **Get feedback** - Ask friends to try it
5. **Keep improving** - Add more modules over time

---

## 📚 Helpful Resources

- **This project's deployment guide**: [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)
- **Quick 3-step deploy**: [QUICK_DEPLOY.md](QUICK_DEPLOY.md)
- **JupyterBook docs**: https://jupyterbook.org
- **GitHub Pages docs**: https://docs.github.com/pages

---

## ✅ You're Ready!

Your ML Learning Platform is ready to deploy. Follow the steps above and you'll have a live website in under 5 minutes!

**Questions?** Check the detailed deployment guide or troubleshooting section.

**Good luck! 🚀**