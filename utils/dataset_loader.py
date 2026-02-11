"""
Dataset loading utilities
Beginner-friendly data loading with automatic caching
"""

import os
import numpy as np
import pandas as pd
from pathlib import Path
from typing import Optional, Tuple, Dict
import pickle


class DatasetLoader:
    """
    Load and cache datasets for the ML learning platform.
    Automatically downloads, caches, and provides beginner-friendly access.
    """
    
    def __init__(self, base_path: str = "."):
        """
        Initialize dataset loader.
        
        Args:
            base_path: Base directory for the learning platform
        """
        self.base_path = Path(base_path)
        self.data_dir = self.base_path / "data"
        self.raw_dir = self.data_dir / "raw"
        self.processed_dir = self.data_dir / "processed"
        
        # Create directories
        self.data_dir.mkdir(exist_ok=True)
        self.raw_dir.mkdir(exist_ok=True)
        self.processed_dir.mkdir(exist_ok=True)
    
    def load_iris(self) -> pd.DataFrame:
        """
        Load Iris flower dataset.
        
        Returns:
            DataFrame with features and target
        """
        from sklearn.datasets import load_iris
        
        iris = load_iris()
        df = pd.DataFrame(iris.data, columns=iris.feature_names)
        df['target'] = iris.target
        df['species'] = df['target'].map({i: name for i, name in enumerate(iris.target_names)})
        
        return df
    
    def load_titanic(self) -> Tuple[pd.DataFrame, pd.DataFrame]:
        """
        Load Titanic survival dataset.
        
        Returns:
            Tuple of (train_df, test_df)
        """
        # Try to download from seaborn
        try:
            import seaborn as sns
            df = sns.load_dataset('titanic')
            
            # Split into train/test
            train_size = int(0.8 * len(df))
            train_df = df[:train_size].copy()
            test_df = df[train_size:].copy()
            
            return train_df, test_df
        except:
            # Create synthetic version if download fails
            print("Warning: Could not download Titanic dataset. Creating synthetic version.")
            return self._create_synthetic_titanic()
    
    def _create_synthetic_titanic(self) -> Tuple[pd.DataFrame, pd.DataFrame]:
        """Create a synthetic Titanic-like dataset."""
        np.random.seed(42)
        n_samples = 891
        
        data = {
            'survived': np.random.binomial(1, 0.38, n_samples),
            'pclass': np.random.choice([1, 2, 3], n_samples, p=[0.25, 0.22, 0.53]),
            'sex': np.random.choice(['male', 'female'], n_samples, p=[0.64, 0.36]),
            'age': np.random.normal(30, 12, n_samples),
            'sibsp': np.random.choice([0, 1, 2, 3, 4, 5, 8], n_samples, p=[0.68, 0.23, 0.03, 0.02, 0.02, 0.01, 0.01]),
            'parch': np.random.choice([0, 1, 2, 3, 4, 5, 6], n_samples, p=[0.76, 0.13, 0.09, 0.01, 0.01, 0.01, 0.01]),
            'fare': np.random.lognormal(3, 1, n_samples),
            'embarked': np.random.choice(['S', 'C', 'Q'], n_samples, p=[0.72, 0.19, 0.09])
        }
        
        df = pd.DataFrame(data)
        df['age'] = df['age'].clip(0, 80)
        
        train_size = int(0.8 * len(df))
        return df[:train_size].copy(), df[train_size:].copy()
    
    def load_boston_housing(self) -> pd.DataFrame:
        """
        Load Boston housing dataset.
        
        Returns:
            DataFrame with housing features and prices
        """
        try:
            from sklearn.datasets import fetch_openml
            data = fetch_openml(name="boston", version=1, as_frame=True, parser='auto')
            df = data.frame
            df['target'] = data.target
            return df
        except:
            print("Warning: Could not load Boston housing. Creating synthetic version.")
            return self._create_synthetic_housing()
    
    def _create_synthetic_housing(self) -> pd.DataFrame:
        """Create synthetic housing data."""
        np.random.seed(42)
        n_samples = 506
        
        data = {
            'CRIM': np.random.lognormal(-2, 1.5, n_samples),
            'ZN': np.random.choice([0, 20, 40, 80, 100], n_samples),
            'INDUS': np.random.beta(2, 5, n_samples) * 30,
            'CHAS': np.random.binomial(1, 0.07, n_samples),
            'NOX': np.random.normal(0.55, 0.1, n_samples),
            'RM': np.random.normal(6.3, 0.7, n_samples),
            'AGE': np.random.beta(2, 1, n_samples) * 100,
            'DIS': np.random.lognormal(1.2, 0.5, n_samples),
            'RAD': np.random.choice(range(1, 25), n_samples),
            'TAX': np.random.choice(range(187, 720, 10), n_samples),
            'PTRATIO': np.random.choice(range(12, 23), n_samples),
            'B': np.random.normal(357, 100, n_samples),
            'LSTAT': np.random.lognormal(3, 0.5, n_samples),
            'target': np.random.lognormal(3, 0.5, n_samples) * 10
        }
        
        return pd.DataFrame(data)
    
    def load_mnist(self, n_samples: Optional[int] = None) -> Tuple[np.ndarray, np.ndarray]:
        """
        Load MNIST handwritten digits dataset.
        
        Args:
            n_samples: Number of samples to load (None = all)
            
        Returns:
            Tuple of (X, y) arrays
        """
        from sklearn.datasets import fetch_openml
        
        try:
            mnist = fetch_openml('mnist_784', version=1, parser='auto', as_frame=False)
            X, y = mnist.data, mnist.target.astype(int)
            
            if n_samples:
                X = X[:n_samples]
                y = y[:n_samples]
            
            return X, y
        except:
            print("Warning: Could not load MNIST. Creating synthetic version.")
            return self._create_synthetic_mnist(n_samples or 70000)
    
    def _create_synthetic_mnist(self, n_samples: int) -> Tuple[np.ndarray, np.ndarray]:
        """Create synthetic MNIST-like data."""
        np.random.seed(42)
        X = np.random.rand(n_samples, 784) * 255
        y = np.random.randint(0, 10, n_samples)
        return X, y
    
    def load_wine_quality(self) -> pd.DataFrame:
        """
        Load wine quality dataset.
        
        Returns:
            DataFrame with wine features and quality scores
        """
        try:
            from sklearn.datasets import fetch_openml
            data = fetch_openml(name='wine-quality-red', version=1, parser='auto', as_frame=True)
            return data.frame
        except:
            print("Warning: Could not load wine quality. Creating synthetic version.")
            return self._create_synthetic_wine()
    
    def _create_synthetic_wine(self) -> pd.DataFrame:
        """Create synthetic wine quality data."""
        np.random.seed(42)
        n_samples = 1599
        
        data = {
            'fixed_acidity': np.random.normal(8.3, 1.7, n_samples),
            'volatile_acidity': np.random.lognormal(-2.1, 0.6, n_samples),
            'citric_acid': np.random.beta(2, 5, n_samples) * 1,
            'residual_sugar': np.random.lognormal(1.5, 0.7, n_samples),
            'chlorides': np.random.lognormal(-5, 0.7, n_samples),
            'free_sulfur_dioxide': np.random.lognormal(3.2, 0.9, n_samples),
            'total_sulfur_dioxide': np.random.lognormal(5.5, 0.7, n_samples),
            'density': np.random.normal(0.9967, 0.002, n_samples),
            'pH': np.random.normal(3.3, 0.15, n_samples),
            'sulphates': np.random.lognormal(-0.8, 0.4, n_samples),
            'alcohol': np.random.normal(10.4, 1.1, n_samples),
            'quality': np.random.choice(range(3, 9), n_samples, p=[0.025, 0.1, 0.43, 0.30, 0.13, 0.015])
        }
        
        return pd.DataFrame(data)
    
    def load_mall_customers(self) -> pd.DataFrame:
        """
        Load mall customer segmentation data.
        
        Returns:
            DataFrame with customer features
        """
        # This is a commonly used synthetic dataset for clustering
        np.random.seed(42)
        n_samples = 200
        
        data = {
            'customer_id': range(1, n_samples + 1),
            'gender': np.random.choice(['Male', 'Female'], n_samples),
            'age': np.random.randint(18, 71, n_samples),
            'annual_income': np.random.randint(15, 140, n_samples),
            'spending_score': np.random.randint(1, 100, n_samples)
        }
        
        return pd.DataFrame(data)
    
    def get_dataset_info(self, dataset_name: str) -> Dict:
        """
        Get information about a dataset.
        
        Args:
            dataset_name: Name of the dataset
            
        Returns:
            Dictionary with dataset information
        """
        info = {
            'iris': {
                'name': 'Iris Flower Dataset',
                'description': 'Classic dataset for classification with 3 species of iris flowers',
                'n_samples': 150,
                'n_features': 4,
                'task': 'Classification',
                'source': 'UCI Machine Learning Repository'
            },
            'titanic': {
                'name': 'Titanic Survival',
                'description': 'Predict survival on the Titanic based on passenger features',
                'n_samples': 891,
                'n_features': 11,
                'task': 'Classification',
                'source': 'Kaggle'
            },
            'boston_housing': {
                'name': 'Boston Housing Prices',
                'description': 'Predict median home values in Boston suburbs',
                'n_samples': 506,
                'n_features': 13,
                'task': 'Regression',
                'source': 'UCI Machine Learning Repository'
            },
            'mnist': {
                'name': 'MNIST Handwritten Digits',
                'description': 'Classify handwritten digits (0-9) from 28x28 images',
                'n_samples': 70000,
                'n_features': 784,
                'task': 'Classification',
                'source': 'Yann LeCun'
            },
            'wine_quality': {
                'name': 'Wine Quality',
                'description': 'Predict wine quality based on physicochemical properties',
                'n_samples': 1599,
                'n_features': 11,
                'task': 'Regression/Classification',
                'source': 'UCI Machine Learning Repository'
            },
            'mall_customers': {
                'name': 'Mall Customer Segmentation',
                'description': 'Customer data for clustering and segmentation analysis',
                'n_samples': 200,
                'n_features': 4,
                'task': 'Clustering',
                'source': 'Synthetic dataset'
            }
        }
        
        return info.get(dataset_name, {'name': dataset_name, 'description': 'Unknown dataset'})
    
    def save_processed_data(self, data, filename: str):
        """
        Save processed data to cache.
        
        Args:
            data: Data to save (DataFrame or numpy array)
            filename: Name of the file
        """
        filepath = self.processed_dir / filename
        
        if isinstance(data, pd.DataFrame):
            data.to_csv(filepath, index=False)
        else:
            np.save(filepath, data)
        
        print(f"Saved processed data to {filepath}")
    
    def load_processed_data(self, filename: str, is_dataframe: bool = True):
        """
        Load processed data from cache.
        
        Args:
            filename: Name of the file
            is_dataframe: Whether the data is a DataFrame
            
        Returns:
            Loaded data
        """
        filepath = self.processed_dir / filename
        
        if not filepath.exists():
            raise FileNotFoundError(f"Processed data not found: {filepath}")
        
        if is_dataframe:
            return pd.read_csv(filepath)
        else:
            return np.load(filepath)


# Convenience functions
def load_iris() -> pd.DataFrame:
    """Load Iris dataset."""
    loader = DatasetLoader()
    return loader.load_iris()


def load_titanic() -> Tuple[pd.DataFrame, pd.DataFrame]:
    """Load Titanic dataset."""
    loader = DatasetLoader()
    return loader.load_titanic()


def load_boston_housing() -> pd.DataFrame:
    """Load Boston housing dataset."""
    loader = DatasetLoader()
    return loader.load_boston_housing()


def load_mnist(n_samples: Optional[int] = None) -> Tuple[np.ndarray, np.ndarray]:
    """Load MNIST dataset."""
    loader = DatasetLoader()
    return loader.load_mnist(n_samples)


def load_wine_quality() -> pd.DataFrame:
    """Load wine quality dataset."""
    loader = DatasetLoader()
    return loader.load_wine_quality()


def load_mall_customers() -> pd.DataFrame:
    """Load mall customer segmentation data."""
    loader = DatasetLoader()
    return loader.load_mall_customers()