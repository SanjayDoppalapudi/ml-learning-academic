# Exercise Set 1: Vector Operations

## Module 1: Mathematical Foundations
**Difficulty**: ⭐ (Beginner)  
**Problems**: 10  
**Estimated Time**: 30 minutes

---

## Instructions

Complete each exercise by filling in the code where indicated. Run the test cells to check your answers.

**Setup:**

```python
import numpy as np
import sys
sys.path.append('../..')
from utils.progress_tracker import get_tracker

tracker = get_tracker()
```

---

## Exercise 1.1: Vector Creation

Create a vector with values [1, 2, 3, 4, 5] using NumPy.

```python
# TODO: Create the vector
vector_1 = None  # Replace None with your code

# Test
expected = np.array([1, 2, 3, 4, 5])
assert np.array_equal(vector_1, expected), "Vector doesn't match expected values"
print("✓ Exercise 1.1 passed!")
tracker.mark_exercise_complete('module_1', 'ex_1_1_1', score=1.0, skill='mathematics')
```

---

## Exercise 1.2: Vector Arithmetic

Given vectors $a = [1, 2, 3]$ and $b = [4, 5, 6]$, compute:
- Element-wise sum
- Element-wise product
- Dot product

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# TODO: Compute the operations
sum_ab = None  # a + b
product_ab = None  # a * b (element-wise)
dot_ab = None  # a · b

# Tests
assert np.array_equal(sum_ab, np.array([5, 7, 9])), "Sum incorrect"
assert np.array_equal(product_ab, np.array([4, 10, 18])), "Product incorrect"
assert dot_ab == 32, "Dot product incorrect"
print("✓ Exercise 1.2 passed!")
tracker.mark_exercise_complete('module_1', 'ex_1_1_2', score=1.0, skill='mathematics')
```

---

## Exercise 1.3: Vector Norm

Calculate the L2 norm (Euclidean length) of vector $v = [3, 4]$.

**Formula**: $\|v\|_2 = \sqrt{v_1^2 + v_2^2}$

```python
v = np.array([3, 4])

# TODO: Calculate L2 norm
# Method 1: Using formula
norm_manual = None

# Method 2: Using numpy
norm_numpy = None

# Test
expected = 5.0
assert abs(norm_manual - expected) < 1e-10, "Manual calculation incorrect"
assert abs(norm_numpy - expected) < 1e-10, "NumPy calculation incorrect"
print("✓ Exercise 1.3 passed!")
tracker.mark_exercise_complete('module_1', 'ex_1_1_3', score=1.0, skill='mathematics')
```

---

## Exercise 1.4: Broadcasting

Use broadcasting to add 10 to every element of the array [1, 2, 3, 4, 5].

```python
arr = np.array([1, 2, 3, 4, 5])

# TODO: Add 10 using broadcasting
result = None

# Test
expected = np.array([11, 12, 13, 14, 15])
assert np.array_equal(result, expected), "Broadcasting incorrect"
print("✓ Exercise 1.4 passed!")
tracker.mark_exercise_complete('module_1', 'ex_1_1_4', score=1.0, skill='mathematics')
```

---

## Exercise 1.5: Vector Indexing

Extract the middle three elements from the vector [10, 20, 30, 40, 50, 60, 70].

```python
vec = np.array([10, 20, 30, 40, 50, 60, 70])

# TODO: Extract middle three elements (30, 40, 50)
middle = None

# Test
expected = np.array([30, 40, 50])
assert np.array_equal(middle, expected), "Indexing incorrect"
print("✓ Exercise 1.5 passed!")
tracker.mark_exercise_complete('module_1', 'ex_1_1_5', score=1.0, skill='mathematics')
```

---

## Exercise 1.6: Vector Statistics

Calculate mean, standard deviation, and sum of vector [2, 4, 6, 8, 10].

```python
data = np.array([2, 4, 6, 8, 10])

# TODO: Calculate statistics
mean_val = None
std_val = None
sum_val = None

# Tests
assert abs(mean_val - 6.0) < 1e-10, "Mean incorrect"
assert abs(std_val - np.std(data, ddof=0)) < 1e-10, "Std incorrect"
assert sum_val == 30, "Sum incorrect"
print("✓ Exercise 1.6 passed!")
tracker.mark_exercise_complete('module_1', 'ex_1_1_6', score=1.0, skill='mathematics')
```

---

## Exercise 1.7: Boolean Indexing

Select all positive values from the array [-2, -1, 0, 1, 2, 3].

```python
arr = np.array([-2, -1, 0, 1, 2, 3])

# TODO: Select positive values
positive = None

# Test
expected = np.array([1, 2, 3])
assert np.array_equal(positive, expected), "Boolean indexing incorrect"
print("✓ Exercise 1.7 passed!")
tracker.mark_exercise_complete('module_1', 'ex_1_1_7', score=1.0, skill='mathematics')
```

---

## Exercise 1.8: Vector Normalization

Normalize vector $v = [3, 4]$ to have unit length (L2 norm = 1).

```python
v = np.array([3, 4])

# TODO: Normalize the vector
v_normalized = None

# Test
norm = np.linalg.norm(v_normalized)
assert abs(norm - 1.0) < 1e-10, f"Norm is {norm}, should be 1.0"
print("✓ Exercise 1.8 passed!")
tracker.mark_exercise_complete('module_1', 'ex_1_1_8', score=1.0, skill='mathematics')
```

---

## Exercise 1.9: Vector Distance

Calculate the Euclidean distance between points $a = [1, 2]$ and $b = [4, 6]$.

**Formula**: $d = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}$

```python
a = np.array([1, 2])
b = np.array([4, 6])

# TODO: Calculate distance
distance = None

# Test
expected = 5.0
assert abs(distance - expected) < 1e-10, "Distance calculation incorrect"
print("✓ Exercise 1.9 passed!")
tracker.mark_exercise_complete('module_1', 'ex_1_1_9', score=1.0, skill='mathematics')
```

---

## Exercise 1.10: Vector Concatenation

Combine vectors [1, 2, 3] and [4, 5, 6] horizontally (side by side) and vertically (stacked).

```python
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])

# TODO: Concatenate
horizontal = None  # Should be [1, 2, 3, 4, 5, 6]
vertical = None    # Should be [[1, 2, 3], [4, 5, 6]]

# Tests
assert np.array_equal(horizontal, np.array([1, 2, 3, 4, 5, 6])), "Horizontal concat incorrect"
assert np.array_equal(vertical, np.array([[1, 2, 3], [4, 5, 6]])), "Vertical concat incorrect"
print("✓ Exercise 1.10 passed!")
tracker.mark_exercise_complete('module_1', 'ex_1_1_10', score=1.0, skill='mathematics')
```

---

## Summary

```python
print("=" * 50)
print("EXERCISE SET 1 COMPLETE!")
print("=" * 50)
print("\n✓ All 10 exercises passed!")
print("✓ Skills practiced: Vector operations, broadcasting, indexing")
print("\n🏆 XP Earned: 100")

# Show progress
stats = tracker.get_stats()
print(f"\nTotal XP: {stats['user']['total_xp']}")
print(f"Mathematics skill level: {stats['skills']['mathematics']['level']}")
```