# Exercise Set 5: Eigendecomposition

## Module 1: Mathematical Foundations
**Difficulty**: ⭐⭐⭐⭐ (Intermediate-Advanced)  
**Problems**: 8  
**Estimated Time**: 45 minutes

---

## Setup

```python
import numpy as np
import sys
sys.path.append('../..')
from utils.progress_tracker import get_tracker

tracker = get_tracker()
```

---

## Exercise 5.1: Characteristic Polynomial

For matrix $A = \begin{bmatrix} 3 & 1 \\ 1 & 3 \end{bmatrix}$, find eigenvalues by solving $\det(A - \lambda I) = 0$.

```python
A = np.array([[3, 1], [1, 3]])

# TODO: Calculate eigenvalues manually
# Characteristic equation: (3-λ)² - 1 = 0
# Expand and solve
lambda1 = None  # Larger eigenvalue
lambda2 = None  # Smaller eigenvalue

# Test
eigenvalues = np.linalg.eigvals(A)
assert abs(lambda1 - max(eigenvalues)) < 1e-10, "Lambda1 incorrect"
assert abs(lambda2 - min(eigenvalues)) < 1e-10, "Lambda2 incorrect"
print(f"✓ Exercise 5.1 passed! Eigenvalues: {lambda1}, {lambda2}")
tracker.mark_exercise_complete('module_1', 'ex_1_5_1', score=1.0, skill='mathematics')
```

---

## Exercise 5.2: Verify Eigenvector

Verify that $v = \begin{bmatrix} 1 \\ 1 \end{bmatrix}$ is an eigenvector of $A = \begin{bmatrix} 4 & 2 \\ 2 & 4 \end{bmatrix}$ and find its eigenvalue.

```python
A = np.array([[4, 2], [2, 4]])
v = np.array([1, 1])

# TODO: Verify eigenvector and find eigenvalue
# If v is eigenvector, then Av = λv
Av = None  # A @ v
eigenvalue = None  # Ratio of (Av)ᵢ / vᵢ

# Test: Check if Av = λv
assert np.allclose(Av, eigenvalue * v), "Not an eigenvector or wrong eigenvalue"
print(f"✓ Exercise 5.2 passed! Eigenvalue = {eigenvalue}")
tracker.mark_exercise_complete('module_1', 'ex_1_5_2', score=1.0, skill='mathematics')
```

---

## Exercise 5.3: Trace and Determinant

For matrix $A = \begin{bmatrix} 5 & 2 \\ 2 & 3 \end{bmatrix}$, verify that:
- $\text{trace}(A) = \sum \lambda_i$
- $\det(A) = \prod \lambda_i$

```python
A = np.array([[5, 2], [2, 3]])

# TODO: Calculate trace, det, and eigenvalues
trace_A = None
det_A = None
eigenvalues = None

# Verify relationships
sum_eigenvalues = None
product_eigenvalues = None

# Tests
assert abs(trace_A - sum_eigenvalues) < 1e-10, "Trace != sum of eigenvalues"
assert abs(det_A - product_eigenvalues) < 1e-10, "Det != product of eigenvalues"
print(f"✓ Exercise 5.3 passed!")
print(f"  Trace = {trace_A}, Sum of λ = {sum_eigenvalues}")
print(f"  Det = {det_A}, Product of λ = {product_eigenvalues}")
tracker.mark_exercise_complete('module_1', 'ex_1_5_3', score=1.0, skill='mathematics')
```

---

## Exercise 5.4: Diagonalization

Diagonalize $A = \begin{bmatrix} 4 & 1 \\ 1 & 4 \end{bmatrix}$ as $A = PDP^{-1}$ where $D$ is diagonal.

```python
A = np.array([[4, 1], [1, 4]])

# TODO: Find P and D
eigenvalues, eigenvectors = np.linalg.eig(A)
P = None  # Matrix of eigenvectors
D = None  # Diagonal matrix of eigenvalues

# Test: Verify A = P @ D @ np.linalg.inv(P)
A_reconstructed = P @ D @ np.linalg.inv(P)
assert np.allclose(A, A_reconstructed), "Diagonalization incorrect"
print("✓ Exercise 5.4 passed! A = PDP^(-1)")
tracker.mark_exercise_complete('module_1', 'ex_1_5_4', score=1.0, skill='mathematics')
```

---

## Exercise 5.5: Power Iteration

Implement power iteration to find the largest eigenvalue of $A = \begin{bmatrix} 3 & 1 \\ 1 & 3 \end{bmatrix}$.

```python
def power_iteration(A, n_iter=20):
    """Find largest eigenvalue using power iteration."""
    n = A.shape[0]
    v = np.random.rand(n)
    v = v / np.linalg.norm(v)  # Normalize
    
    for _ in range(n_iter):
        # TODO: Power iteration step
        Av = None      # A @ v
        v = None       # Normalize Av
        eigenvalue = None  # Rayleigh quotient: v^T @ A @ v
    
    return eigenvalue, v

# Test
A = np.array([[3, 1], [1, 3]])
largest_eig, eigvec = power_iteration(A)
expected = 4  # Largest eigenvalue of [[3,1],[1,3]] is 4
assert abs(largest_eig - expected) < 0.01, f"Power iteration incorrect: {largest_eig}"
print(f"✓ Exercise 5.5 passed! Largest eigenvalue ≈ {largest_eig:.6f}")
tracker.mark_exercise_complete('module_1', 'ex_1_5_5', score=1.0, skill='mathematics')
```

---

## Exercise 5.6: SVD Components

For matrix $A = \begin{bmatrix} 3 & 0 \\ 0 & 2 \end{bmatrix}$, compute SVD and verify $A = U\Sigma V^T$.

```python
A = np.array([[3, 0], [0, 2]])

# TODO: Compute SVD
U, S, Vt = None, None, None  # np.linalg.svd(A)

# Reconstruct
Sigma = None  # np.diag(S)
A_reconstructed = None  # U @ Sigma @ Vt

# Tests
assert np.allclose(A, A_reconstructed), "SVD reconstruction failed"
assert np.allclose(U.T @ U, np.eye(2)), "U not orthogonal"
assert np.allclose(Vt @ Vt.T, np.eye(2)), "V not orthogonal"
print(f"✓ Exercise 5.6 passed!")
print(f"  Singular values: {S}")
tracker.mark_exercise_complete('module_1', 'ex_1_5_6', score=1.0, skill='mathematics')
```

---

## Exercise 5.7: Low-Rank Approximation

Create the best rank-1 approximation of $A = \begin{bmatrix} 3 & 2 \\ 2 & 3 \end{bmatrix}$ using SVD.

```python
A = np.array([[3, 2], [2, 3]], dtype=float)

# TODO: Compute rank-1 approximation
U, S, Vt = np.linalg.svd(A)

# Keep only top component
U1 = None  # U[:, :1]
S1 = None  # S[:1]
Vt1 = None  # Vt[:1, :]

A_rank1 = None  # U1 @ np.diag(S1) @ Vt1

# Calculate approximation error
error = None  # Frobenius norm: np.linalg.norm(A - A_rank1)

print(f"✓ Exercise 5.7 passed!")
print(f"  Rank-1 approximation error: {error:.6f}")
tracker.mark_exercise_complete('module_1', 'ex_1_5_7', score=1.0, skill='mathematics')
```

---

## Exercise 5.8: PCA Variance

Given covariance matrix $\Sigma = \begin{bmatrix} 10 & 3 \\ 3 & 5 \end{bmatrix}$, calculate the percentage of variance captured by the first principal component.

```python
Sigma = np.array([[10, 3], [3, 5]], dtype=float)

# TODO: Find eigenvalues of covariance matrix
eigenvalues = None  # np.linalg.eigvals(Sigma)
eigenvalues_sorted = None  # Sort descending

# Calculate variance explained
variance_explained = None  # Largest eigenvalue / sum of all eigenvalues

# Test
assert variance_explained > 0.5, "First PC should capture > 50% variance"
print(f"✓ Exercise 5.8 passed!")
print(f"  First PC captures {variance_explained:.2%} of variance")
tracker.mark_exercise_complete('module_1', 'ex_1_5_8', score=1.0, skill='mathematics')
```

---

## Summary

```python
print("=" * 50)
print("EXERCISE SET 5 COMPLETE!")
print("=" * 50)
print("\n✓ All 8 exercises passed!")
print("✓ Skills practiced: Eigendecomposition, SVD, PCA")
print("\n🏆 XP Earned: 80")

stats = tracker.get_stats()
print(f"\nTotal XP: {stats['user']['total_xp']}")
print(f"Mathematics skill level: {stats['skills']['mathematics']['level']}")

# Check for Mathematician achievement
if stats['skills']['mathematics']['exercises_completed'] >= 46:
    print("\n🏆 ACHIEVEMENT UNLOCKED: Mathematician!")
    print("   Completed all Module 1 exercises!")
```