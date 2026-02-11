# Module 1 Exercises

## Practice Problems for Mathematical Foundations

This folder contains exercise sets to reinforce the concepts learned in Module 1 projects.

## 📚 Exercise Sets

### [Set 1: Vector Operations](set_1_vectors.md)
**Difficulty**: ⭐ Beginner  
**Problems**: 10  
**Time**: 30 minutes  
**Topics**: Array creation, broadcasting, indexing, vector math

### [Set 2: Matrix Operations](set_2_matrices.md)
**Difficulty**: ⭐⭐ Beginner-Intermediate  
**Problems**: 10  
**Time**: 40 minutes  
**Topics**: Matrix creation, multiplication, transpose, inverse, determinants

### [Set 3: Transformations](set_3_transformations.md)
**Difficulty**: ⭐⭐⭐ Intermediate  
**Problems**: 8  
**Time**: 45 minutes  
**Topics**: Rotation, scaling, shearing, combined transformations

### [Set 4: Optimization](set_4_optimization.md)
**Difficulty**: ⭐⭐⭐ Intermediate  
**Problems**: 10  
**Time**: 50 minutes  
**Topics**: Derivatives, gradient descent, learning rates, convergence

### [Set 5: Eigendecomposition](set_5_eigendecomposition.md)
**Difficulty**: ⭐⭐⭐⭐ Intermediate-Advanced  
**Problems**: 8  
**Time**: 45 minutes  
**Topics**: Eigenvalues, eigenvectors, SVD, PCA, diagonalization

## 🎯 Total Practice

- **46 Problems** across all sets
- **~3.5 hours** of practice
- **460 XP** available
- Achievement unlocks at 80% completion

## 💡 How to Use

1. Complete each exercise set after the corresponding project
2. Run the test cells to verify your answers
3. Track your progress automatically
4. Check solutions if stuck (separate solutions folder)

## 🏆 Achievement

**Mathematician**: Score 80%+ on all exercise sets to unlock this achievement!

## 📊 Progress Tracking

Your progress is automatically saved. View your stats:

```python
from utils.progress_tracker import get_tracker
tracker = get_tracker()
stats = tracker.get_stats()
print(f"Exercises completed: {stats['summary']['exercises_completed']}")
print(f"Mathematics level: {stats['skills']['mathematics']['level']}")
```