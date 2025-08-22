import pandas as pd
import pytest
from life_expectancy.cleaner import clean_data
from pathlib import Path

def test_clean_data_fixture(raw_life_expectancy_eu_file, expected_life_expectancy_eu_file):
    df_clean = clean_data(raw_life_expectancy_eu_file, region='PT')
    pd.testing.assert_frame_equal(
        df_clean.reset_index(drop=True),
        expected_life_expectancy_eu_file.reset_index(drop=True)
    )
