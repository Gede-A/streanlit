import pandas as pd

def fetch_data():
    return pd.DataFrame({
        'category': ['A', 'B', 'C', 'A', 'B', 'C'],
        'value': [10, 20, 30, 40, 50, 60]
    })

def process_data(data):
    data['processed_column'] = data['value'] * 2  
    return data
