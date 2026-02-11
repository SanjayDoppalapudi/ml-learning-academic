# Exercise Set 3: Transformations

## Module 1: Mathematical Foundations
**Difficulty**: ⭐⭐⭐ (Intermediate)  
**Problems**: 8  
**Estimated Time**: 45 minutes

---

## Setup

```python
import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append('../..')
from utils.progress_tracker import get_tracker

tracker = get_tracker()
```

---

## Exercise 3.1: Rotation Matrix

Create a rotation matrix for 90 degrees counterclockwise.

```python
def get_rotation_matrix_90():
    """Return rotation matrix for 90 degrees CCW."""
    # TODO: Create rotation matrix
    R = None
    return R

# Test
R = get_rotation_matrix_90()
expected = np.array([[0, -1], [1, 0]])
assert np.allclose(R, expected), "Rotation matrix incorrect"

# Verify: Apply to [1, 0] should give [0, 1]
v = np.array([1, 0])
rotated = R @ v
assert np.allclose(rotated, [0, 1]), "Rotation doesn't work correctly"
print("✓ Exercise 3.1 passed!")
tracker.mark_exercise_complete('module_1', 'ex_1_3_1', score=1.0, skill='mathematics')
```

---

## Exercise 3.2: Apply Transformation

Apply transformation matrix $T = \begin{bmatrix} 2 & 0 \\ 0 & 3 \end{bmatrix}$ to vector $v = \begin{bmatrix} 1 \\ 1 \end{bmatrix}$.

```python
T = np.array([[2, 0], [0, 3]])
v = np.array([1, 1])

# TODO: Apply transformation
v_transformed = None

# Test
expected = np.array([2, 3])
assert np.allclose(v_transformed, expected), "Transformation incorrect"
print("✓ Exercise 3.2 passed!")
tracker.mark_exercise_complete('module_1', 'ex_1_3_2', score=1.0, skill='mathematics')
```

---

## Exercise 3.3: Combined Transformations

First rotate by 45°, then scale by 2 in both directions. What is the combined transformation matrix?

```python
def get_combined_transformation():
    """Return combined rotation (45°) then scaling (2x)."""
    # TODO: Create matrices and combine them
    theta = np.pi / 4  # 45 degrees
    R = None  # Rotation matrix
    S = None  # Scaling matrix
    T = None  # Combined: S @ R
    return T

# Test
T = get_combined_transformation()
# Verify by applying to unit vector
v = np.array([1, 0])
result = T @ v
expected_length = 2  # Scaled by 2
actual_length = np.linalg.norm(result)
assert abs(actual_length - expected_length) < 1e-10, "Combined transformation incorrect"
print("✓ Exercise 3.3 passed!")
tracker.mark_exercise_complete('module_1', 'ex_1_3_3', score=1.0, skill='mathematics')
```

---

## Exercise 3.4: Shearing Matrix

Create a horizontal shearing matrix with factor 0.5 and apply it to the unit square.

```python
def shear_points(points, shear_factor):
    """Apply horizontal shear to a set of 2D points."""
    # TODO: Create shearing matrix and apply
    Sh = None
    sheared = None
    return sheared

# Test with unit square
square = np.array([[0, 0], [1, 0], [1, 1], [0, 1], [0, 0]]).T
sheared_square = shear_points(square, 0.5)

# After horizontal shear by 0.5:
# Point (0, 1) should move to (0.5, 1)
assert np.allclose(sheared_square[:, 2], [1.5, 1]), "Shearing incorrect"
print("✓ Exercise 3.4 passed!")
tracker.mark_exercise_complete('module_1', 'ex_1_3_4', score=1.0, skill='mathematics')
```

---

## Exercise 3.5: Determinant of Transformation

Calculate the determinant of a scaling matrix that scales x by 3 and y by 2. What does this tell you about area?

```python
# Create scaling matrix
S = np.array([[3, 0], [0, 2]])

# TODO: Calculate determinant
det_S = None

# Test
expected = 6  # Area scales by factor of 6
assert abs(det_S - expected) < 1e-10, "Determinant calculation incorrect"
print(f"✓ Exercise 3.5 passed! Determinant = {det_S} (area scaling factor)")
tracker.mark_exercise_complete('module_1', 'ex_1_3_5', score=1.0, skill='mathematics')
```

---

## Exercise 3.6: Inverse Transformation

Find the inverse of a rotation matrix for 30 degrees and verify it rotates by -30 degrees.

```python
def get_inverse_rotation_30():
    """Return inverse of 30-degree rotation matrix."""
    # TODO: Calculate rotation matrix and its inverse
    theta = np.pi / 6  # 30 degrees
    R = None
    R_inv = None
    return R_inv

# Test
R_inv = get_inverse_rotation_30()
v = np.array([0, 1])
rotated_back = R_inv @ v

# Original vector rotated 30° CCW from x-axis
# After inverse rotation, should be close to original
# Let's verify by checking R @ R_inv = I
theta = np.pi / 6
R = np.array([[np.cos(theta), -np.sin(theta)],
              [np.sin(theta), np.cos(theta)]])
identity_check = R @ R_inv
assert np.allclose(identity_check, np.eye(2)), "Inverse rotation incorrect"
print("✓ Exercise 3.6 passed!")
tracker.mark_exercise_complete('module_1', 'ex_1_3_6', score=1.0, skill='mathematics')
```

---

## Exercise 3.7: Eigenvalues of Transformation

Find the eigenvalues of the scaling matrix $S = \begin{bmatrix} 2 & 0 \\ 0 & 3 \end{bmatrix}$. What do they represent?

```python
S = np.array([[2, 0], [0, 3]])

# TODO: Calculate eigenvalues
eigenvalues = None

# Test
expected = np.array([2, 3])
assert np.allclose(sorted(eigenvalues), sorted(expected)), "Eigenvalues incorrect"
print(f"✓ Exercise 3.7 passed! Eigenvalues: {eigenvalues} (scaling factors)")
tracker.mark_exercise_complete('module_1', 'ex_1_3_7', score=1.0, skill='mathematics')
```

---

## Exercise 3.8: Transform a Circle

Generate points on a circle, apply a non-uniform scaling (2x in x, 0.5x in y), and verify it becomes an ellipse.

```python
# Generate circle points
theta = np.linspace(0, 2*np.pi, 100)
circle = np.array([np.cos(theta), np.sin(theta)])

# TODO: Apply non-uniform scaling
S = None  # Scaling matrix
ellipse = None  # S @ circle

# Test: Check that points form an ellipse
# Major axis should be along x (radius 2), minor along y (radius 0.5)
x_max = np.max(ellipse[0])
y_max = np.max(ellipse[1])
assert abs(x_max - 2.0) < 0.1, "Ellipse x-radius incorrect"
assert abs(y_max - 0.5) < 0.1, "Ellipse y-radius incorrect"
print("✓ Exercise 3.8 passed! Circle transformed to ellipse")
tracker.mark_exercise_complete('module_1', 'ex_1_3_8', score=1.0, skill='mathematics')
```

---

## Summary

```python
print("=" * 50)
print("EXERCISE SET 3 COMPLETE!")
print("=" * 50)
print("\n✓ All 8 exercises passed!")
print("✓ Skills practiced: Rotation, scaling, shearing, eigenvalues")
print("\n🏆 XP Earned: 80")

stats = tracker.get_stats()
print(f"\nTotal XP: {stats['user']['total_xp']}")
```