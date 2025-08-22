'''
This module contains the function that saves the data.
'''
from pathlib import Path
import pandas as pd

def save_data(df: pd.DataFrame, output_dir: str = "./life_expectancy/data", filename: str = None):
    """Saves the DataFrame to a CSV file."""
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    if filename is None:
        filename = "life_expectancy.csv"
    file_path = output_path / filename
    df.to_csv(file_path, index=False)
