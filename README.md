# Machine Learning Learning Platform
## Academic Curriculum - Project-Based Learning

A comprehensive, project-first machine learning curriculum designed for systematic learning with academic rigor.

### 📚 Curriculum Overview

This platform contains **22 hands-on projects** across **5 core modules** plus **3 capstone projects**, progressing from foundational mathematics to deep learning.

#### Modules

1. **Module 0: Python Foundation** (Reference)
   - NumPy, Pandas, Matplotlib refresher
   - Quick reference for Python essentials

2. **Module 1: Mathematical Foundations** (8 hours)
   - Project 1.1: Array Operations & Broadcasting
   - Project 1.2: Image Transformations
   - Project 1.3: Function Optimization
   - Project 1.4: Dimensionality Reduction

3. **Module 2: Statistical Inference** (8 hours)
   - Project 2.1: Descriptive Analysis
   - Project 2.2: Probability Distributions
   - Project 2.3: Hypothesis Testing
   - Project 2.4: Bayesian Inference

4. **Module 3: Machine Learning Algorithms** (12 hours)
   - Project 3.1: Linear Regression from Scratch
   - Project 3.2: Logistic Regression from Scratch
   - Project 3.3: Decision Trees
   - Project 3.4: K-Means Clustering
   - Project 3.5: Model Evaluation

5. **Module 4: Neural Networks & Deep Learning** (12 hours)
   - Project 4.1: Perceptron from Scratch
   - Project 4.2: Multi-Layer Perceptron (NumPy)
   - Project 4.3: Introduction to PyTorch
   - Project 4.4: MNIST Digit Classifier

6. **Capstone Projects** (15 hours each)
   - Regression Challenge: House Price Prediction
   - Classification Challenge: Customer Churn
   - Deep Learning Challenge: Image Classification

### 🚀 Quick Start

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Launch JupyterLab:**
   ```bash
   jupyter lab
   ```

3. **Start with Module 0** if you need a Python refresher, or jump to **Module 1** to begin learning.

4. **Track your progress:** Progress is automatically saved to `logs/` and synced via Git.

### 📊 Progress Tracking

Your learning journey is automatically tracked:
- Study time per session
- Exercises completed
- Projects finished
- Concept mastery ratings
- Weekly and monthly reports

View your progress dashboard anytime by running:
```python
from utils.progress_tracker import show_dashboard
show_dashboard()
```

### 📁 Project Structure

```
ml-learning-academic/
├── config/               # Configuration files
├── utils/                # Helper scripts and tools
├── data/                 # Datasets (raw and processed)
├── module_*/             # Learning modules
├── capstone_projects/    # End-to-end projects
├── exports/              # PDF, Python script exports
└── logs/                 # Progress and session logs
```

### 📄 Exports

Each notebook can be exported to:
- **PDF**: Academic paper format
- **Python Script** (.py): Runnable code
- **HTML**: Interactive web format

Use the export function in any notebook:
```python
from utils.notebook_converter import export_notebook
export_notebook('path/to/notebook.ipynb', format='pdf')
```

### ☁️ Cloud Sync

The platform supports automatic sync to:
- **Google Drive**: Daily backups
- **Dropbox**: Cross-device access
- **Git**: Version control and history

Configure sync in `config/cloud_sync.py`.

### 🎯 Learning Path

**Week 1-2**: Module 1 (Mathematical Foundations)  
**Week 3-4**: Module 2 (Statistical Inference)  
**Week 5-8**: Module 3 (ML Algorithms)  
**Week 9-12**: Module 4 (Deep Learning)  
**Week 13+**: Capstone Projects

*Note: Timeline is flexible. Learn at your own pace.*

### 📖 Academic Style

All materials follow academic standards:
- Structured with Abstract, Introduction, Methodology, Results, Discussion
- Mathematical formulations with LaTeX
- Cited references and further reading
- Publication-quality visualizations
- Comprehensive exercises with solutions

### 🏆 Achievement System

Track your accomplishments:
- **Scholar**: Complete first module
- **Mathematician**: Master mathematical foundations
- **Statistician**: Complete statistical inference module
- **ML Engineer**: Build 5 algorithms from scratch
- **Deep Learning Expert**: Achieve 95%+ on capstone
- **Master**: Complete entire curriculum

### 🔧 System Requirements

- Python 3.8+
- 4GB RAM (8GB recommended)
- 5GB disk space
- Git (for version control)
- Google Drive or Dropbox account (optional, for cloud sync)

### 📧 Support

For issues or questions:
- Check the exercises/solutions folder
- Review theory_supplements for additional explanations
- Consult the README in each module folder

### 📜 License

This educational content is for personal use. Feel free to modify and adapt for your learning needs.

---

**Happy Learning!** 🎓

*Remember: The goal is not just to complete projects, but to deeply understand the concepts. Take your time, experiment, and enjoy the journey.*