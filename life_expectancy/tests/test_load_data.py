import pandas as pd
import pytest
from life_expectancy.loader import load_data
from pathlib import Path

def test_load_data():
    # Use the fixture file as a test input
    fixture_path = Path(__file__).parent / "fixtures" / "eu_life_expectancy_raw.tsv"
    df = load_data(str(fixture_path))
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
