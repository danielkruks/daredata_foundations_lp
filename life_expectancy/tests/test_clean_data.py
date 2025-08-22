'''
This module contains the testing of the clean_data function.
'''
from life_expectancy.cleaner import clean_data
import pandas as pd

def test_clean_data_fixture(raw_life_expectancy_eu_file, expected_life_expectancy_eu_file):
    '''
    This function tests the clean_data function using the mock data creates and 
    stored in the fixtures folder
    '''
    df_clean = clean_data(raw_life_expectancy_eu_file, region='PT')
    pd.testing.assert_frame_equal(
        df_clean.reset_index(drop=True),
        expected_life_expectancy_eu_file.reset_index(drop=True)
    )
