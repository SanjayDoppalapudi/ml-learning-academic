# Exercise Set 4: Optimization

## Module 1: Mathematical Foundations
**Difficulty**: ⭐⭐⭐ (Intermediate)  
**Problems**: 10  
**Estimated Time**: 50 minutes

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

## Exercise 4.1: Numerical Derivative

Calculate the numerical derivative of $f(x) = x^3$ at $x = 2$ using $h = 0.001$.

```python
def f(x):
    return x**3

x = 2.0
h = 0.001

# TODO: Calculate numerical derivative using (f(x+h) - f(x-h)) / (2h)
derivative = None

# Test: f'(x) = 3x², so at x=2: f'(2) = 12
expected = 12.0
assert abs(derivative - expected) < 0.01, f"Derivative incorrect: {derivative}"
print(f"✓ Exercise 4.1 passed! f'(2) ≈ {derivative:.6f}")
tracker.mark_exercise_complete('module_1', 'ex_1_4_1', score=1.0, skill='mathematics')
```

---

## Exercise 4.2: Gradient Descent Step

Given $f(x) = (x-5)^2$ and current position $x_0 = 8$, perform one gradient descent step with learning rate $\alpha = 0.3$.

```python
def f(x):
    return (x - 5)**2

def df(x):
    """Derivative of f."""
    return 2 * (x - 5)

x0 = 8.0
alpha = 0.3

# TODO: Perform one GD step
x1 = None  # x0 - alpha * df(x0)

# Test
expected = 6.2  # 8 - 0.3 * 2 * (8-5) = 8 - 1.8 = 6.2
assert abs(x1 - expected) < 1e-10, f"GD step incorrect: {x1}"
print(f"✓ Exercise 4.2 passed! x1 = {x1}")
tracker.mark_exercise_complete('module_1', 'ex_1_4_2', score=1.0, skill='mathematics')
```

---

## Exercise 4.3: Convergence Check

Implement a convergence check that returns True if $|x_{new} - x_{old}| < tolerance$.

```python
def has_converged(x_old, x_new, tolerance=1e-6):
    """Check if optimization has converged."""
    # TODO: Implement convergence check
    converged = None
    return converged

# Tests
assert has_converged(1.0, 1.0000001, tolerance=1e-6) == True, "Should converge"
assert has_converged(1.0, 1.1, tolerance=1e-6) == False, "Should not converge"
print("✓ Exercise 4.3 passed!")
tracker.mark_exercise_complete('module_1', 'ex_1_4_3', score=1.0, skill='mathematics')
```

---

## Exercise 4.4: Learning Rate Impact

For $f(x) = x^2$, calculate the first 3 GD steps with different learning rates: $\alpha = 0.1, 0.5, 1.0$, starting from $x_0 = 2$.

```python
def gradient_descent_steps(x0, alpha, n_steps):
    """Perform n_steps of GD on f(x)=x²."""
    x = x0
    history = [x]
    
    for _ in range(n_steps):
        # TODO: Implement GD step for f(x) = x²
        gradient = None  # f'(x) = 2x
        x = None         # x - alpha * gradient
        history.append(x)
    
    return history

# Test
history = gradient_descent_steps(2.0, 0.1, 3)
# Expected: [2.0, 1.6, 1.28, 1.024]
expected = [2.0, 1.6, 1.28, 1.024]
assert np.allclose(history, expected), f"GD steps incorrect: {history}"
print("✓ Exercise 4.4 passed!")
tracker.mark_exercise_complete('module_1', 'ex_1_4_4', score=1.0, skill='mathematics')
```

---

## Exercise 4.5: 2D Gradient

Calculate the gradient of $f(x, y) = x^2 + 3y^2$ at point $(2, 1)$.

```python
def f(x, y):
    return x**2 + 3*y**2

def gradient_f(x, y):
    """Return gradient [df/dx, df/dy]."""
    # TODO: Calculate partial derivatives
    df_dx = None  # ∂f/∂x = 2x
    df_dy = None  # ∂f/∂y = 6y
    return np.array([df_dx, df_dy])

# Test at point (2, 1)
grad = gradient_f(2, 1)
expected = np.array([4, 6])
assert np.allclose(grad, expected), f"Gradient incorrect: {grad}"
print(f"✓ Exercise 4.5 passed! Gradient at (2,1): {grad}")
tracker.mark_exercise_complete('module_1', 'ex_1_4_5', score=1.0, skill='mathematics')
```

---

## Exercise 4.6: Cost Function

Implement the Mean Squared Error cost function: $MSE = \frac{1}{n}\sum_{i=1}^n (y_i - \hat{y}_i)^2$

```python
def mse(y_true, y_pred):
    """Calculate Mean Squared Error."""
    # TODO: Implement MSE
    error = None
    return error

# Test
y_true = np.array([1, 2, 3, 4, 5])
y_pred = np.array([1.1, 1.9, 3.2, 3.8, 5.1])
mse_value = mse(y_true, y_pred)
expected = np.mean((y_true - y_pred)**2)
assert abs(mse_value - expected) < 1e-10, "MSE calculation incorrect"
print(f"✓ Exercise 4.6 passed! MSE = {mse_value:.6f}")
tracker.mark_exercise_complete('module_1', 'ex_1_4_6', score=1.0, skill='mathematics')
```

---

## Exercise 4.7: Learning Rate Decay

Implement learning rate decay: $\alpha_t = \alpha_0 / (1 + decay \cdot t)$

```python
def learning_rate_decay(alpha0, decay, t):
    """Calculate learning rate at time step t with decay."""
    # TODO: Implement decay formula
    alpha_t = None
    return alpha_t

# Test
alpha0 = 0.1
decay = 0.01
alpha_10 = learning_rate_decay(alpha0, decay, 10)
expected = 0.1 / (1 + 0.01 * 10)  # = 0.1 / 1.1 ≈ 0.0909
assert abs(alpha_10 - expected) < 1e-10, "LR decay incorrect"
print(f"✓ Exercise 4.7 passed! α₁₀ = {alpha_10:.6f}")
tracker.mark_exercise_complete('module_1', 'ex_1_4_7', score=1.0, skill='mathematics')
```

---

## Exercise 4.8: Find Minimum

Use gradient descent to find the minimum of $f(x) = (x-3)^2 + 2$. Start at $x=0$ with $\alpha=0.1$ for 100 iterations.

```python
def find_minimum_gd(x0=0.0, alpha=0.1, n_iter=100):
    """Find minimum of f(x) = (x-3)² + 2 using GD."""
    x = x0
    
    for _ in range(n_iter):
        # TODO: Gradient descent update
        gradient = None  # f'(x) = 2(x-3)
        x = None         # Update rule
    
    return x

# Test
x_min = find_minimum_gd()
expected = 3.0  # Minimum at x=3
assert abs(x_min - expected) < 0.01, f"Minimum incorrect: {x_min}"
print(f"✓ Exercise 4.8 passed! Minimum at x = {x_min:.6f}")
tracker.mark_exercise_complete('module_1', 'ex_1_4_8', score=1.0, skill='mathematics')
```

---

## Exercise 4.9: Momentum

Implement gradient descent with momentum: $v_t = \beta v_{t-1} + (1-\beta)g_t$, then $x_t = x_{t-1} - \alpha v_t$

```python
def gd_with_momentum(x0, alpha=0.1, beta=0.9, n_iter=50):
    """GD with momentum on f(x)=x², starting at x0=5."""
    x = x0
    v = 0
    
    for _ in range(n_iter):
        gradient = 2 * x  # f'(x) = 2x
        # TODO: Update velocity and position
        v = None  # βv + (1-β)g
        x = None  # x - αv
    
    return x

# Test
x_final = gd_with_momentum(5.0)
assert abs(x_final) < 0.1, f"Did not converge to 0: {x_final}"
print(f"✓ Exercise 4.9 passed! Final x = {x_final:.6f}")
tracker.mark_exercise_complete('module_1', 'ex_1_4_9', score=1.0, skill='mathematics')
```

---

## Exercise 4.10: Convexity Check

Check if function $f(x) = x^4$ is convex by verifying if the second derivative is always non-negative.

```python
def is_convex_x4(x_range=np.linspace(-2, 2, 100)):
    """Check if f(x)=x⁴ is convex on given range."""
    # Second derivative of x⁴ is 12x²
    second_derivative = None  # Calculate 12x² for all x in range
    
    # TODO: Check if all second derivatives >= 0
    is_conv = None
    return is_conv

# Test
convex = is_convex_x4()
assert convex == True, "x⁴ should be convex"
print("✓ Exercise 4.10 passed! f(x)=x⁴ is convex")
tracker.mark_exercise_complete('module_1', 'ex_1_4_10', score=1.0, skill='mathematics')
```

---

## Summary

```python
print("=" * 50)
print("EXERCISE SET 4 COMPLETE!")
print("=" * 50)
print("\n✓ All 10 exercises passed!")
print("✓ Skills practiced: Gradient descent, learning rates, convergence")
print("\n🏆 XP Earned: 100")

stats = tracker.get_stats()
print(f"\nTotal XP: {stats['user']['total_xp']}")
```