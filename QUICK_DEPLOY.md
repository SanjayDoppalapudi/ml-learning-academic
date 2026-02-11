# 🚀 Quick Deploy (3 Steps)

## Step 1: Create Repository ⏱️ 1 minute

1. Go to **https://github.com/new**
2. Name: `ml-learning-platform`
3. Select **Public**
4. Click **Create repository**

![Step 1](https://i.imgur.com/placeholder1.png)

## Step 2: Push Code ⏱️ 1 minute

Run this in your terminal:

```bash
cd ml-learning-academic
./deploy.sh your_username ml-learning-platform
```

Or manually:

```bash
cd ml-learning-academic
git remote add origin https://github.com/YOUR_USERNAME/ml-learning-platform.git
git branch -M main
git push -u origin main
```

## Step 3: Enable Pages ⏱️ 1 minute

1. Go to your repo on GitHub
2. Click **Settings** → **Pages** (left sidebar)
3. Source: **Deploy from a branch**
4. Branch: **gh-pages** / **(root)**
5. Click **Save**

![Step 3](https://i.imgur.com/placeholder2.png)

---

## ✅ Done!

Your site will be live at:
```
https://YOUR_USERNAME.github.io/ml-learning-platform
```

⏳ Wait 2-3 minutes for first deployment

---

## 🔄 Auto-Deployment

After setup, every time you push to main:
1. GitHub Actions automatically builds
2. Updates your website
3. No manual steps needed!

```bash
# Just push your changes
git add .
git commit -m "Add new content"
git push origin main
# Site updates automatically!
```

---

## 🆘 Troubleshooting

**Site not updating?**
- Check Actions tab for build errors
- Ensure repository is public
- Wait 3-5 minutes

**404 errors?**
- Verify file paths in `_toc.yml`
- Check GitHub Pages source is set to gh-pages

**Build fails?**
- Check Python dependencies in requirements.txt
- Look at error messages in Actions tab

---

## 📱 Test Your Site

Once deployed, verify:
- [ ] Homepage loads
- [ ] Module navigation works
- [ ] Projects display correctly
- [ ] Exercises are accessible
- [ ] Mobile view works

**Your ML Learning Platform is now live! 🎉**