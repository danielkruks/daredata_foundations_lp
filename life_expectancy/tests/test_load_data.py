'''
This module tests the load_data function.
'''
from pathlib import Path
import pandas as pd
from life_expectancy.loader import load_data

def test_load_data():
    '''
    This function tests the load_data function using the created mock data file.
    '''
    # Use the fixture file as a test input
    fixture_path = Path(__file__).parent / "fixtures" / "eu_life_expectancy_raw.tsv"
    df = load_data(str(fixture_path))
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
