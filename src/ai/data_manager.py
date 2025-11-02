# coding: utf-8
"""
AI Data Manager - Prepares and normalizes market data
Code Source: Standard ML data preprocessing examples
"""
import pandas as pd
import numpy as np
from typing import Dict

class DataManager:
    def __init__(self):
        self.scaler = None
    
    def normalize_features(self, data: pd.DataFrame) -> pd.DataFrame:
        """Normalize market data features for AI training"""
        # Based on scikit-learn preprocessing patterns
        normalized_data = data.copy()
        for column in data.select_dtypes(include=[np.number]).columns:
            if data[column].std() > 0:
                normalized_data[column] = (data[column] - data[column].mean()) / data[column].std()
        return normalized_data
    
    def create_rolling_features(self, data: pd.DataFrame, window: int = 10) -> pd.DataFrame:
        """Create rolling window features for time series data"""
        # Based on pandas rolling feature patterns
        data['rolling_mean'] = data['price'].rolling(window=window).mean()
        data['rolling_std'] = data['price'].rolling(window=window).std()
        return data.dropna()
