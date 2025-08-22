'''
This module contains the testing of the save_data function.
It is done using a mock version of data
'''
from unittest.mock import patch
import pandas as pd
from life_expectancy.saver import save_data

def test_save_data_mock():
    '''
    This function tests the save_data function by mocking the to_csv method.
    For more information check: Assignment 3 -> Step 3
    '''
    df = pd.DataFrame({
        'unit': ['Y'], 'sex': ['M'], 'age': ['TOTAL'], 'region': ['PT'],
        'year': [2020], 'value': [80.0]
    })
    with patch.object(pd.DataFrame, 'to_csv') as mock_to_csv:
        save_data(df, output_dir='fake_dir', filename='fake_file.csv')
        mock_to_csv.assert_called_once()
