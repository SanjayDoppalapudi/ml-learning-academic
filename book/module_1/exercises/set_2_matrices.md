# Exercise Set 2: Matrix Operations

## Module 1: Mathematical Foundations
**Difficulty**: ⭐⭐ (Beginner-Intermediate)  
**Problems**: 10  
**Estimated Time**: 40 minutes

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

## Exercise 2.1: Matrix Creation

Create a 3×3 identity matrix and a 2×3 matrix of ones.

```python
# TODO: Create matrices
identity_3x3 = None  # 3x3 identity matrix
ones_2x3 = None      # 2x3 matrix of ones

# Tests
assert identity_3x3.shape == (3, 3), "Identity matrix shape incorrect"
assert np.allclose(identity_3x3, np.eye(3)), "Identity matrix values incorrect"
assert ones_2x3.shape == (2, 3), "Ones matrix shape incorrect"
assert np.all(ones_2x3 == 1), "Ones matrix values incorrect"
print("✓ Exercise 2.1 passed!")
tracker.mark_exercise_complete('module_1', 'ex_1_2_1', score=1.0, skill='mathematics')
```

---

## Exercise 2.2: Matrix Multiplication

Multiply matrices $A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}$ and $B = \begin{bmatrix} 5 & 6 \\ 7 & 8 \end{bmatrix}$.

```python
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# TODO: Matrix multiplication
C = None

# Test
expected = np.array([[19, 22], [43, 50]])
assert np.array_equal(C, expected), "Matrix multiplication incorrect"
print("✓ Exercise 2.2 passed!")
tracker.mark_exercise_complete('module_1', 'ex_1_2_2', score=1.0, skill='mathematics')
```

---

## Exercise 2.3: Matrix Transpose

Compute the transpose of matrix $M = \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{bmatrix}$.

```python
M = np.array([[1, 2, 3], [4, 5, 6]])

# TODO: Transpose
M_T = None

# Test
expected = np.array([[1, 4], [2, 5], [3, 6]])
assert np.array_equal(M_T, expected), "Transpose incorrect"
assert M_T.shape == (3, 2), "Transpose shape incorrect"
print("✓ Exercise 2.3 passed!")
tracker.mark_exercise_complete('module_1', 'ex_1_2_3', score=1.0, skill='mathematics')
```

---

## Exercise 2.4: Matrix Indexing

Extract the submatrix consisting of rows 1-2 and columns 0-1 from:

$$A = \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{bmatrix}$$

```python
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# TODO: Extract submatrix
submatrix = None

# Test
expected = np.array([[4, 5], [7, 8]])
assert np.array_equal(submatrix, expected), "Submatrix extraction incorrect"
print("✓ Exercise 2.4 passed!")
tracker.mark_exercise_complete('module_1', 'ex_1_2_4', score=1.0, skill='mathematics')
```

---

## Exercise 2.5: Matrix Determinant

Calculate the determinant of matrix $A = \begin{bmatrix} 4 & 2 \\ 1 & 3 \end{bmatrix}$.

**Formula**: $\det(A) = ad - bc$ for $\begin{bmatrix} a & b \\ c & d \end{bmatrix}$

```python
A = np.array([[4, 2], [1, 3]])

# TODO: Calculate determinant
det_manual = None  # Using formula
det_numpy = None   # Using np.linalg.det

# Test
expected = 10  # 4*3 - 2*1
assert abs(det_manual - expected) < 1e-10, "Manual determinant incorrect"
assert abs(det_numpy - expected) < 1e-10, "NumPy determinant incorrect"
print("✓ Exercise 2.5 passed!")
tracker.mark_exercise_complete('module_1', 'ex_1_2_5', score=1.0, skill='mathematics')
```

---

## Exercise 2.6: Matrix Inverse

Find the inverse of matrix $A = \begin{bmatrix} 4 & 7 \\ 2 & 6 \end{bmatrix}$.

```python
A = np.array([[4, 7], [2, 6]])

# TODO: Calculate inverse
A_inv = None

# Test: A @ A_inv should be identity
identity_check = A @ A_inv
assert np.allclose(identity_check, np.eye(2)), "Inverse incorrect"
print("✓ Exercise 2.6 passed!")
tracker.mark_exercise_complete('module_1', 'ex_1_2_6', score=1.0, skill='mathematics')
```

---

## Exercise 2.7: Matrix Broadcasting

Add vector $v = [10, 20, 30]$ to each row of matrix $M = \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{bmatrix}$.

```python
M = np.array([[1, 2, 3], [4, 5, 6]])
v = np.array([10, 20, 30])

# TODO: Broadcasting addition
result = None

# Test
expected = np.array([[11, 22, 33], [14, 25, 36]])
assert np.array_equal(result, expected), "Broadcasting incorrect"
print("✓ Exercise 2.7 passed!")
tracker.mark_exercise_complete('module_1', 'ex_1_2_7', score=1.0, skill='mathematics')
```

---

## Exercise 2.8: Matrix Statistics

Given matrix $M = \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{bmatrix}$, calculate:
- Sum of all elements
- Mean of each column
- Maximum of each row

```python
M = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# TODO: Calculate statistics
total_sum = None
column_means = None
row_maxs = None

# Tests
assert total_sum == 45, "Total sum incorrect"
assert np.allclose(column_means, [4, 5, 6]), "Column means incorrect"
assert np.array_equal(row_maxs, [3, 6, 9]), "Row maximums incorrect"
print("✓ Exercise 2.8 passed!")
tracker.mark_exercise_complete('module_1', 'ex_1_2_8', score=1.0, skill='mathematics')
```

---

## Exercise 2.9: Solve Linear System

Solve $Ax = b$ where $A = \begin{bmatrix} 3 & 1 \\ 1 & 2 \end{bmatrix}$ and $b = \begin{bmatrix} 9 \\ 8 \end{bmatrix}$.

```python
A = np.array([[3, 1], [1, 2]])
b = np.array([9, 8])

# TODO: Solve for x
x = None

# Test
expected = np.array([2, 3])  # 3*2 + 1*3 = 9, 1*2 + 2*3 = 8
assert np.allclose(x, expected), "Solution incorrect"
print("✓ Exercise 2.9 passed!")
tracker.mark_exercise_complete('module_1', 'ex_1_2_9', score=1.0, skill='mathematics')
```

---

## Exercise 2.10: Matrix Reshaping

Reshape a 1D array [1, 2, 3, 4, 5, 6] into a 2×3 matrix.

```python
arr = np.array([1, 2, 3, 4, 5, 6])

# TODO: Reshape
matrix = None

# Test
expected = np.array([[1, 2, 3], [4, 5, 6]])
assert np.array_equal(matrix, expected), "Reshape incorrect"
assert matrix.shape == (2, 3), "Reshape shape incorrect"
print("✓ Exercise 2.10 passed!")
tracker.mark_exercise_complete('module_1', 'ex_1_2_10', score=1.0, skill='mathematics')
```

---

## Summary

```python
print("=" * 50)
print("EXERCISE SET 2 COMPLETE!")
print("=" * 50)
print("\n✓ All 10 exercises passed!")
print("✓ Skills practiced: Matrix operations, broadcasting, linear algebra")
print("\n🏆 XP Earned: 100")

stats = tracker.get_stats()
print(f"\nTotal XP: {stats['user']['total_xp']}")
```