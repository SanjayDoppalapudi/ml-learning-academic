"""
ML Learning Platform Utilities
Utilities for progress tracking, visualizations, and data loading
"""

from .progress_tracker import ProgressTracker, get_tracker
from .visualizations import (
    setup_figure, plot_vector_2d, plot_matrix_heatmap,
    plot_function_1d, plot_gradient_descent_path, plot_distribution,
    plot_confusion_matrix, plot_learning_curve, plot_decision_boundary,
    create_progress_dashboard, quick_plot
)
from .notebook_converter import NotebookConverter, export_notebook, batch_export_module
from .dataset_loader import (
    DatasetLoader, load_iris, load_titanic, load_boston_housing,
    load_mnist, load_wine_quality, load_mall_customers
)

__all__ = [
    'ProgressTracker', 'get_tracker',
    'setup_figure', 'plot_vector_2d', 'plot_matrix_heatmap',
    'plot_function_1d', 'plot_gradient_descent_path', 'plot_distribution',
    'plot_confusion_matrix', 'plot_learning_curve', 'plot_decision_boundary',
    'create_progress_dashboard', 'quick_plot',
    'NotebookConverter', 'export_notebook', 'batch_export_module',
    'DatasetLoader', 'load_iris', 'load_titanic', 'load_boston_housing',
    'load_mnist', 'load_wine_quality', 'load_mall_customers'
]