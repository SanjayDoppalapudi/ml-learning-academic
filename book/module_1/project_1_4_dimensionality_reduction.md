# Project 1.4: Dimensionality Reduction
## PCA and SVD for Image Compression

**Module**: Mathematical Foundations  
**Project ID**: 1.4  
**Estimated Time**: 75 minutes  
**Prerequisites**: Projects 1.1-1.3  

### Learning Objectives
By the end of this project, you will be able to:
- [ ] Understand eigenvalues and eigenvectors
- [ ] Apply SVD for matrix factorization
- [ ] Implement PCA for dimensionality reduction
- [ ] Compress images using low-rank approximations

### Mathematical Concepts Covered
- **Eigendecomposition**: Breaking down linear transformations
- **SVD**: Singular Value Decomposition
- **PCA**: Principal Component Analysis
- **Low-rank approximation**: Compression techniques

---

## Abstract

This project introduces dimensionality reduction through eigendecomposition, SVD, and PCA. You will implement image compression using low-rank matrix approximations and apply PCA to visualize high-dimensional data in lower dimensions. These techniques are fundamental for data compression, noise reduction, and feature extraction in machine learning.

## 1. Introduction

Dimensionality reduction is crucial for:
- **Data compression**: Reducing storage requirements
- **Noise reduction**: Filtering out less important features
- **Visualization**: Plotting high-dimensional data in 2D/3D
- **Speed**: Faster computations on lower-dimensional data

### Real-World Applications
- **Image compression**: JPEG uses similar techniques
- **Face recognition**: Eigenfaces for identification
- **Recommendation systems**: Matrix factorization (Netflix prize)
- **Genomics**: Analyzing gene expression data

---

## 2. Theoretical Background

### 2.1 Eigenvalues and Eigenvectors

For a square matrix $A$, eigenvectors $v$ and eigenvalues $\lambda$ satisfy:

$$Av = \lambda v$$

**Interpretation**: Eigenvectors are directions that remain unchanged (except for scaling) when transformed by $A$.

### 2.2 Singular Value Decomposition (SVD)

Any matrix $A$ can be decomposed as:

$$A = U \Sigma V^T$$

Where:
- $U$: Left singular vectors (orthogonal)
- $\Sigma$: Singular values (diagonal)
- $V^T$: Right singular vectors (orthogonal)

### 2.3 Low-Rank Approximation

Using only top-$k$ singular values:

$$A_k = U_k \Sigma_k V_k^T \approx A$$

This gives the best rank-$k$ approximation!

### 2.4 Principal Component Analysis (PCA)

PCA finds directions of maximum variance:

1. Center the data
2. Compute covariance matrix
3. Find eigenvectors of covariance matrix
4. Project data onto top-$k$ eigenvectors

---

## 3. Implementation

### 3.1 Setup

```python
import numpy as np
import matplotlib.pyplot as plt

%matplotlib inline
plt.style.use('seaborn-v0_8-whitegrid')

print("✓ Libraries imported")
```

### 3.2 Eigendecomposition Example

```python
# Create a symmetric matrix
A = np.array([[4, 2],
              [2, 3]])

print("Matrix A:")
print(A)

# Compute eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

print("\nEigenvalues:", eigenvalues)
print("\nEigenvectors (columns):")
print(eigenvectors)

# Verify: A @ v = lambda * v
print("\nVerification:")
for i in range(len(eigenvalues)):
    lhs = A @ eigenvectors[:, i]
    rhs = eigenvalues[i] * eigenvectors[:, i]
    print(f"Eigenvector {i+1}: {np.allclose(lhs, rhs)}")
```

**Visualization:**

```python
# Plot transformation effect
circle = np.array([[np.cos(t), np.sin(t)] 
                   for t in np.linspace(0, 2*np.pi, 100)])
transformed = circle @ A.T

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.plot(circle[:, 0], circle[:, 1], 'b-', label='Original')
plt.plot(transformed[:, 0], transformed[:, 1], 'r-', label='Transformed')
# Draw eigenvectors
for i in range(2):
    vec = eigenvectors[:, i] * eigenvalues[i]
    plt.arrow(0, 0, vec[0], vec[1], head_width=0.3, 
              color='green', linewidth=2)
plt.axis('equal')
plt.legend()
plt.title('Eigendecomposition Visualization')
plt.grid(True, alpha=0.3)

plt.subplot(1, 2, 2)
plt.bar(range(1, len(eigenvalues)+1), eigenvalues, color='steelblue')
plt.xlabel('Eigenvalue Index')
plt.ylabel('Value')
plt.title('Eigenvalues')
plt.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.show()
```

### 3.3 SVD Implementation

```python
# Create a sample matrix
size = 50
x = np.linspace(-3, 3, size)
y = np.linspace(-3, 3, size)
X, Y = np.meshgrid(x, y)
image = np.sin(X) * np.cos(Y) + 0.5 * np.sin(3*X) * np.cos(2*Y)

# Perform SVD
U, S, Vt = np.linalg.svd(image, full_matrices=False)

print(f"Original shape: {image.shape}")
print(f"U shape: {U.shape}, S shape: {S.shape}, Vt shape: {Vt.shape}")
print(f"\nTop 10 singular values: {S[:10]}")

# Verify reconstruction
reconstructed = U @ np.diag(S) @ Vt
error = np.mean((image - reconstructed)**2)
print(f"\nReconstruction error: {error:.2e}")
```

**Visualize SVD Components:**

```python
fig, axes = plt.subplots(2, 3, figsize=(15, 10))

axes[0, 0].imshow(image, cmap='viridis')
axes[0, 0].set_title('Original Image')
axes[0, 0].axis('off')

axes[0, 1].imshow(U[:, :5], cmap='viridis', aspect='auto')
axes[0, 1].set_title('U (First 5 columns)')
axes[0, 1].axis('off')

axes[0, 2].imshow(Vt[:5, :], cmap='viridis', aspect='auto')
axes[0, 2].set_title('V^T (First 5 rows)')
axes[0, 2].axis('off')

axes[1, 0].semilogy(S, 'b-', linewidth=2)
axes[1, 0].set_xlabel('Index')
axes[1, 0].set_ylabel('Singular Value (log scale)')
axes[1, 0].set_title('Singular Values')
axes[1, 0].grid(True, alpha=0.3)

# Cumulative energy
cumulative_energy = np.cumsum(S**2) / np.sum(S**2)
axes[1, 1].plot(cumulative_energy, 'r-', linewidth=2)
axes[1, 1].axhline(y=0.9, color='g', linestyle='--', label='90% energy')
axes[1, 1].set_xlabel('Number of Components')
axes[1, 1].set_ylabel('Cumulative Energy')
axes[1, 1].set_title('Energy Retention')
axes[1, 1].legend()
axes[1, 1].grid(True, alpha=0.3)

axes[1, 2].imshow(reconstructed, cmap='viridis')
axes[1, 2].set_title('Reconstructed (Full SVD)')
axes[1, 2].axis('off')

plt.tight_layout()
plt.show()
```

### 3.4 Image Compression with Low-Rank Approximation

```python
def compress_image_svd(image, k):
    """
    Compress image using rank-k SVD approximation.
    """
    # Perform SVD
    U, S, Vt = np.linalg.svd(image, full_matrices=False)
    
    # Keep only top k components
    U_k = U[:, :k]
    S_k = S[:k]
    Vt_k = Vt[:k, :]
    
    # Reconstruct
    compressed = U_k @ np.diag(S_k) @ Vt_k
    
    # Calculate compression ratio
    original_size = image.size
    compressed_size = U_k.size + S_k.size + Vt_k.size
    compression_ratio = compressed_size / original_size
    
    return compressed, compression_ratio

# Test with different k values
k_values = [5, 10, 20, 50]

fig, axes = plt.subplots(2, 3, figsize=(15, 10))

# Original
axes[0, 0].imshow(image, cmap='viridis')
axes[0, 0].set_title(f'Original\nSize: {image.size} elements')
axes[0, 0].axis('off')

# Compressed versions
for idx, k in enumerate(k_values):
    compressed, ratio = compress_image_svd(image, k)
    error = np.mean((image - compressed)**2)
    
    row = (idx + 1) // 3
    col = (idx + 1) % 3
    
    axes[row, col].imshow(compressed, cmap='viridis')
    axes[row, col].set_title(f'k={k}\nRatio: {ratio:.2%}\nMSE: {error:.4f}')
    axes[row, col].axis('off')

plt.suptitle('Image Compression Using SVD', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()

print("\n✓ Image compression demonstrated")
print(f"Original size: {image.size} elements")
print(f"With k=20: Only {20*(image.shape[0]+image.shape[1]+1)} elements needed")
```

### 3.5 Principal Component Analysis (PCA)

```python
def pca_2d_visualization():
    """Demonstrate PCA on 2D data."""
    
    # Generate correlated 2D data
    np.random.seed(42)
    n_points = 200
    
    x = np.random.randn(n_points)
    y = 2 * x + np.random.randn(n_points) * 0.5
    
    data = np.column_stack([x, y])
    
    # Center the data
    mean = np.mean(data, axis=0)
    centered_data = data - mean
    
    # Compute covariance matrix
    cov_matrix = np.cov(centered_data.T)
    
    # Eigendecomposition
    eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)
    
    # Sort by eigenvalue
    idx = eigenvalues.argsort()[::-1]
    eigenvalues = eigenvalues[idx]
    eigenvectors = eigenvectors[:, idx]
    
    # Project data
    projected = centered_data @ eigenvectors
    
    # Visualization
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))
    
    # Original data
    axes[0].scatter(data[:, 0], data[:, 1], alpha=0.6, s=50)
    axes[0].set_xlabel('X')
    axes[0].set_ylabel('Y')
    axes[0].set_title('Original Data', fontweight='bold')
    axes[0].grid(True, alpha=0.3)
    axes[0].axis('equal')
    
    # With principal components
    axes[1].scatter(data[:, 0], data[:, 1], alpha=0.6, s=50)
    for i in range(2):
        vec = eigenvectors[:, i] * np.sqrt(eigenvalues[i]) * 2
        axes[1].arrow(mean[0], mean[1], vec[0], vec[1],
                     head_width=0.3, color='red' if i == 0 else 'green',
                     linewidth=3, label=f'PC{i+1}')
    axes[1].set_title('Data with Principal Components', fontweight='bold')
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)
    axes[1].axis('equal')
    
    # Projected data
    axes[2].scatter(projected[:, 0], projected[:, 1], 
                   alpha=0.6, s=50, c='purple')
    axes[2].set_xlabel('First Principal Component')
    axes[2].set_ylabel('Second Principal Component')
    axes[2].set_title('Data in PCA Space', fontweight='bold')
    axes[2].grid(True, alpha=0.3)
    axes[2].axis('equal')
    
    plt.tight_layout()
    plt.show()
    
    print(f"\nExplained Variance Ratio:")
    explained_var = eigenvalues / eigenvalues.sum()
    print(f"PC1: {explained_var[0]:.2%}")
    print(f"PC2: {explained_var[1]:.2%}")
    
    return eigenvalues, eigenvectors

# Run PCA visualization
eig_vals, eig_vecs = pca_2d_visualization()
```

---

## 4. Results

### Summary

| Method | Components | Compression | Quality |
|--------|-----------|-------------|---------|
| k=5 | 5 | ~10% | Acceptable |
| k=10 | 10 | ~20% | Good |
| k=20 | 20 | ~40% | Very Good |
| k=50 | 50 | ~100% | Near-perfect |

### Key Findings

1. **Eigendecomposition reveals structure**: Eigenvectors show principal directions
2. **SVD provides optimal compression**: Best rank-k approximation
3. **PCA reduces dimensionality**: Keeps maximum variance directions
4. **Trade-off exists**: Compression vs quality

---

## 5. Discussion

### Applications

- **Face recognition**: Eigenfaces method
- **Recommendation systems**: Matrix factorization
- **Noise reduction**: Keep only significant components
- **Feature extraction**: PCA preprocessing

### Limitations

- **Linear only**: Use kernel PCA for non-linear data
- **Gaussian assumption**: Works best with normal distributions
- **Outlier sensitivity**: Affected by extreme values

### Improvements

- **Incremental SVD**: For large datasets
- **Randomized SVD**: Faster approximations
- **Non-linear methods**: t-SNE, UMAP for visualization

---

## 6. Conclusion

You have successfully:
- Computed eigendecomposition and understood eigenvectors
- Implemented SVD and low-rank approximation
- Compressed images using SVD
- Applied PCA for dimensionality reduction

**Next Steps**: Module 2 - Statistical Inference!

---

## 7. Exercises

### Exercise 1: Eigenvalue Computation

Compute eigenvalues and eigenvectors for:

```python
A = np.array([[5, 2],
              [2, 3]])
```

Verify that $Av = \lambda v$ for each eigenpair.

### Exercise 2: Compression Ratio

For a 1000×1000 image, calculate:
1. Original size (elements)
2. Compressed size with k=50
3. Compression ratio

### Exercise 3: PCA Variance

What percentage of variance is captured by the first principal component if eigenvalues are [10, 2, 1, 0.5]?

---

## Track Your Progress

```python
import sys
sys.path.append('../..')
from utils.progress_tracker import get_tracker

tracker = get_tracker()
tracker.mark_lesson_complete('module_1', 'project_1_4_dimensionality_reduction', xp_earned=60)

print("✓ PROJECT 1.4 COMPLETED!")
print("\n🎉 MODULE 1 COMPLETE!")
print("You are now a Mathematician!")

stats = tracker.get_stats()
print(f"\n🏆 Total XP: {stats['user']['total_xp']}")
print(f"📊 Level: {stats['user']['current_level']}")
print(f"\n🚀 Ready for Module 2: Statistical Inference")
```