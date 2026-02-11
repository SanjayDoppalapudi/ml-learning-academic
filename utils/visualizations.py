"""
Visualization utilities for ML Learning Platform
Publication-quality plots and interactive visualizations
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.patches import FancyBboxPatch
import seaborn as sns
from typing import Optional, List, Tuple, Any

# Set academic style
plt.style.use('seaborn-v0_8-whitegrid')
matplotlib.rcParams['font.size'] = 11
matplotlib.rcParams['axes.labelsize'] = 12
matplotlib.rcParams['axes.titlesize'] = 14
matplotlib.rcParams['xtick.labelsize'] = 10
matplotlib.rcParams['ytick.labelsize'] = 10
matplotlib.rcParams['legend.fontsize'] = 10
matplotlib.rcParams['figure.titlesize'] = 16


def setup_figure(figsize: Tuple[int, int] = (10, 6), dpi: int = 100):
    """Create a figure with academic styling."""
    fig, ax = plt.subplots(figsize=figsize, dpi=dpi)
    return fig, ax


def plot_vector_2d(vector: np.ndarray, 
                   origin: Tuple[float, float] = (0, 0),
                   label: Optional[str] = None,
                   color: str = 'blue',
                   ax=None):
    """
    Plot a 2D vector.
    
    Args:
        vector: 2D vector [x, y]
        origin: Starting point (x, y)
        label: Vector label
        color: Vector color
        ax: Matplotlib axis (creates new if None)
    """
    if ax is None:
        fig, ax = setup_figure()
    
    ax.quiver(origin[0], origin[1], vector[0], vector[1],
              angles='xy', scale_units='xy', scale=1,
              color=color, width=0.005, label=label)
    
    # Add label at tip
    if label:
        ax.text(vector[0] + origin[0] + 0.1, vector[1] + origin[1] + 0.1,
                label, fontsize=11)
    
    # Set equal aspect ratio
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    
    return ax


def plot_matrix_heatmap(matrix: np.ndarray, 
                        title: str = "Matrix Visualization",
                        cmap: str = 'RdBu_r',
                        ax=None):
    """
    Plot a matrix as a heatmap.
    
    Args:
        matrix: 2D numpy array
        title: Plot title
        cmap: Colormap
        ax: Matplotlib axis
    """
    if ax is None:
        fig, ax = setup_figure()
    
    im = ax.imshow(matrix, cmap=cmap, aspect='auto')
    
    # Add colorbar
    cbar = plt.colorbar(im, ax=ax)
    cbar.set_label('Value', rotation=270, labelpad=20)
    
    # Add values to cells
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            text = ax.text(j, i, f'{matrix[i, j]:.2f}',
                          ha="center", va="center", color="black", fontsize=9)
    
    ax.set_title(title, pad=20)
    ax.set_xlabel('Column')
    ax.set_ylabel('Row')
    
    return ax


def plot_function_1d(func, 
                     x_range: Tuple[float, float] = (-10, 10),
                     n_points: int = 1000,
                     title: str = "Function Plot",
                     label: Optional[str] = None,
                     ax=None):
    """
    Plot a 1D mathematical function.
    
    Args:
        func: Function to plot (accepts x, returns y)
        x_range: (min, max) x values
        n_points: Number of points to evaluate
        title: Plot title
        label: Function label for legend
        ax: Matplotlib axis
    """
    if ax is None:
        fig, ax = setup_figure()
    
    x = np.linspace(x_range[0], x_range[1], n_points)
    y = func(x)
    
    ax.plot(x, y, linewidth=2, label=label)
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.set_title(title)
    ax.grid(True, alpha=0.3)
    ax.axhline(y=0, color='k', linewidth=0.5)
    ax.axvline(x=0, color='k', linewidth=0.5)
    
    if label:
        ax.legend()
    
    return ax


def plot_gradient_descent_path(func, 
                               path: List[np.ndarray],
                               x_range: Tuple[float, float] = (-10, 10),
                               title: str = "Gradient Descent Path",
                               ax=None):
    """
    Plot the path of gradient descent on a 1D function.
    
    Args:
        func: Objective function
        path: List of x positions during optimization
        x_range: Range for plotting
        title: Plot title
        ax: Matplotlib axis
    """
    if ax is None:
        fig, ax = setup_figure()
    
    # Plot function
    x = np.linspace(x_range[0], x_range[1], 1000)
    y = func(x)
    ax.plot(x, y, 'b-', linewidth=2, label='f(x)', alpha=0.7)
    
    # Plot path
    path_x = np.array(path)
    path_y = func(path_x)
    
    ax.scatter(path_x, path_y, c='red', s=100, zorder=5, label='Iterations')
    ax.plot(path_x, path_y, 'r--', alpha=0.5)
    
    # Annotate start and end
    ax.annotate('Start', xy=(path_x[0], path_y[0]), xytext=(path_x[0]+1, path_y[0]+1),
                arrowprops=dict(arrowstyle='->', color='green'),
                fontsize=10, color='green')
    ax.annotate('End', xy=(path_x[-1], path_y[-1]), xytext=(path_x[-1]+1, path_y[-1]+1),
                arrowprops=dict(arrowstyle='->', color='purple'),
                fontsize=10, color='purple')
    
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.set_title(title)
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    return ax


def plot_distribution(data: np.ndarray,
                      dist_type: str = 'hist',
                      title: str = "Distribution",
                      bins: int = 30,
                      ax=None):
    """
    Plot data distribution.
    
    Args:
        data: 1D array of data points
        dist_type: 'hist', 'kde', or 'both'
        title: Plot title
        bins: Number of bins for histogram
        ax: Matplotlib axis
    """
    if ax is None:
        fig, ax = setup_figure()
    
    if dist_type == 'hist':
        ax.hist(data, bins=bins, alpha=0.7, color='steelblue', edgecolor='black')
    elif dist_type == 'kde':
        sns.kdeplot(data, ax=ax, fill=True, color='steelblue')
    else:  # both
        ax.hist(data, bins=bins, alpha=0.5, color='steelblue', 
                density=True, edgecolor='black', label='Histogram')
        sns.kdeplot(data, ax=ax, color='red', linewidth=2, label='KDE')
        ax.legend()
    
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency' if dist_type == 'hist' else 'Density')
    ax.set_title(title)
    ax.grid(True, alpha=0.3, axis='y')
    
    # Add statistics
    mean_val = np.mean(data)
    std_val = np.std(data)
    ax.axvline(mean_val, color='red', linestyle='--', linewidth=2, label=f'Mean: {mean_val:.2f}')
    ax.text(0.02, 0.95, f'μ = {mean_val:.2f}\nσ = {std_val:.2f}',
            transform=ax.transAxes, verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    return ax


def plot_confusion_matrix(cm: np.ndarray,
                        classes: List[str],
                        title: str = "Confusion Matrix",
                        cmap = plt.cm.Blues,
                        ax=None):
    """
    Plot confusion matrix.
    
    Args:
        cm: Confusion matrix (n_classes x n_classes)
        classes: List of class names
        title: Plot title
        cmap: Colormap
        ax: Matplotlib axis
    """
    if ax is None:
        fig, ax = setup_figure()
    
    im = ax.imshow(cm, interpolation='nearest', cmap=cmap)
    ax.figure.colorbar(im, ax=ax)
    
    # Set ticks
    ax.set(xticks=np.arange(cm.shape[1]),
           yticks=np.arange(cm.shape[0]),
           xticklabels=classes, yticklabels=classes,
           title=title,
           ylabel='True label',
           xlabel='Predicted label')
    
    # Rotate tick labels
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")
    
    # Add text annotations
    thresh = cm.max() / 2.
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            ax.text(j, i, format(cm[i, j], 'd'),
                   ha="center", va="center",
                   color="white" if cm[i, j] > thresh else "black")
    
    return ax


def plot_learning_curve(train_scores: List[float],
                       val_scores: List[float],
                       title: str = "Learning Curve",
                       ax=None):
    """
    Plot training and validation learning curves.
    
    Args:
        train_scores: Training scores over epochs/iterations
        val_scores: Validation scores over epochs/iterations
        title: Plot title
        ax: Matplotlib axis
    """
    if ax is None:
        fig, ax = setup_figure()
    
    epochs = range(1, len(train_scores) + 1)
    
    ax.plot(epochs, train_scores, 'b-', linewidth=2, label='Training')
    ax.plot(epochs, val_scores, 'r-', linewidth=2, label='Validation')
    
    ax.set_xlabel('Epoch')
    ax.set_ylabel('Score')
    ax.set_title(title)
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    # Highlight best validation score
    best_epoch = np.argmax(val_scores)
    best_score = val_scores[best_epoch]
    ax.axvline(best_epoch + 1, color='green', linestyle='--', alpha=0.5)
    ax.scatter([best_epoch + 1], [best_score], color='green', s=100, zorder=5)
    ax.text(best_epoch + 1, best_score, f'  Best: {best_score:.3f}', 
            fontsize=9, color='green')
    
    return ax


def plot_decision_boundary(X: np.ndarray,
                          y: np.ndarray,
                          model,
                          title: str = "Decision Boundary",
                          ax=None):
    """
    Plot decision boundary for 2D classification.
    
    Args:
        X: Feature matrix (n_samples, 2)
        y: Labels (n_samples,)
        model: Fitted classifier with predict method
        title: Plot title
        ax: Matplotlib axis
    """
    if ax is None:
        fig, ax = setup_figure()
    
    # Create mesh
    h = 0.02
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))
    
    # Predict
    mesh_points = np.c_[xx.ravel(), yy.ravel()]
    Z = model.predict(mesh_points)
    Z = Z.reshape(xx.shape)
    
    # Plot
    ax.contourf(xx, yy, Z, alpha=0.4, cmap=plt.cm.RdYlBu)
    scatter = ax.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.RdYlBu, edgecolors='black')
    ax.set_xlabel('Feature 1')
    ax.set_ylabel('Feature 2')
    ax.set_title(title)
    
    # Add legend
    legend = ax.legend(*scatter.legend_elements(), title="Classes")
    ax.add_artist(legend)
    
    return ax


def create_progress_dashboard(stats: dict):
    """
    Create a visual dashboard of learning progress.
    
    Args:
        stats: Statistics dictionary from ProgressTracker
        
    Returns:
        Matplotlib figure
    """
    fig = plt.figure(figsize=(16, 10), dpi=100)
    
    # Title
    fig.suptitle('ML Learning Progress Dashboard', fontsize=20, fontweight='bold', y=0.98)
    
    # Grid layout
    gs = fig.add_gridspec(3, 3, hspace=0.3, wspace=0.3)
    
    # 1. Overall progress pie chart
    ax1 = fig.add_subplot(gs[0, 0])
    completed = stats['summary']['modules_completed']
    total = stats['summary']['total_modules']
    remaining = total - completed
    
    ax1.pie([completed, remaining], 
            labels=['Completed', 'Remaining'],
            autopct='%1.0f%%',
            colors=['#2ecc71', '#ecf0f1'],
            startangle=90)
    ax1.set_title('Module Completion', fontweight='bold')
    
    # 2. Study time bar chart
    ax2 = fig.add_subplot(gs[0, 1:])
    modules = list(stats['user']['modules'].keys())
    times = [stats['user']['modules'][m]['time_spent_minutes'] / 60 
             for m in modules]
    
    bars = ax2.bar(range(len(modules)), times, color='#3498db', edgecolor='black')
    ax2.set_xticks(range(len(modules)))
    ax2.set_xticklabels([m.replace('_', ' ').title() for m in modules], rotation=45, ha='right')
    ax2.set_ylabel('Hours')
    ax2.set_title('Study Time per Module', fontweight='bold')
    ax2.grid(axis='y', alpha=0.3)
    
    # Add value labels on bars
    for bar in bars:
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.1f}h',
                ha='center', va='bottom', fontsize=9)
    
    # 3. Skills radar chart
    ax3 = fig.add_subplot(gs[1, 0], projection='polar')
    skills = list(stats['skills'].keys())
    levels = [stats['skills'][s]['level'] for s in skills]
    confidence = [stats['skills'][s]['confidence'] for s in skills]
    
    angles = np.linspace(0, 2 * np.pi, len(skills), endpoint=False).tolist()
    levels += levels[:1]
    confidence += confidence[:1]
    angles += angles[:1]
    
    ax3.plot(angles, levels, 'o-', linewidth=2, label='Level', color='#e74c3c')
    ax3.fill(angles, levels, alpha=0.25, color='#e74c3c')
    ax3.plot(angles, confidence, 'o-', linewidth=2, label='Confidence', color='#3498db')
    ax3.fill(angles, confidence, alpha=0.25, color='#3498db')
    
    ax3.set_xticks(angles[:-1])
    ax3.set_xticklabels([s.replace('_', ' ').title() for s in skills])
    ax3.set_ylim(0, 10)
    ax3.set_title('Skills Overview', fontweight='bold', pad=20)
    ax3.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
    
    # 4. Recent activity timeline
    ax4 = fig.add_subplot(gs[1, 1:])
    if stats['recent_sessions']:
        dates = [s['start_time'][:10] for s in stats['recent_sessions']]
        durations = [s['duration_minutes'] for s in stats['recent_sessions']]
        
        ax4.barh(range(len(dates)), durations, color='#9b59b6', edgecolor='black')
        ax4.set_yticks(range(len(dates)))
        ax4.set_yticklabels(dates)
        ax4.set_xlabel('Minutes')
        ax4.set_title('Recent Study Sessions', fontweight='bold')
        ax4.grid(axis='x', alpha=0.3)
        
        # Add duration labels
        for i, v in enumerate(durations):
            ax4.text(v + 1, i, f'{v:.0f} min', va='center', fontsize=9)
    else:
        ax4.text(0.5, 0.5, 'No recent activity', 
                ha='center', va='center', transform=ax4.transAxes)
        ax4.set_title('Recent Study Sessions', fontweight='bold')
    
    # 5. XP and Level progress
    ax5 = fig.add_subplot(gs[2, :2])
    level = stats['user']['current_level']
    xp = stats['user']['total_xp']
    xp_for_next = level * 1000
    xp_current_level = xp % 1000
    
    ax5.barh(['Current Progress'], [xp_current_level], color='#f39c12', height=0.5)
    ax5.barh(['Current Progress'], [xp_for_next], color='#ecf0f1', height=0.5, 
             left=[xp_current_level], label=f'To Level {level + 1}')
    
    ax5.set_xlim(0, xp_for_next)
    ax5.set_xlabel('XP')
    ax5.set_title(f'Level {level} Progress ({xp} total XP)', fontweight='bold')
    ax5.text(xp_current_level/2, 0, f'{xp_current_level}/{xp_for_next}',
            ha='center', va='center', fontweight='bold', color='white')
    
    # 6. Achievements
    ax6 = fig.add_subplot(gs[2, 2])
    achievements = stats['achievements']
    unlocked = sum(1 for a in achievements.values() if a['unlocked'])
    total_achievements = len(achievements)
    
    ax6.pie([unlocked, total_achievements - unlocked],
            labels=['Unlocked', 'Locked'],
            autopct='%1.0f%%',
            colors=['#f1c40f', '#95a5a6'],
            startangle=90)
    ax6.set_title(f'Achievements ({unlocked}/{total_achievements})', fontweight='bold')
    
    return fig


# Convenience function for quick plots
def quick_plot(x, y, title="Quick Plot", xlabel="X", ylabel="Y"):
    """Create a quick line plot."""
    fig, ax = setup_figure()
    ax.plot(x, y, linewidth=2)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    return fig, ax