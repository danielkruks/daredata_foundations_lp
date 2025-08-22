"""Pytest configuration file"""
from pathlib import Path
import pandas as pd
import pytest

from . import FIXTURES_DIR


@pytest.fixture
def raw_life_expectancy_eu_file():
    '''
    Defining the raw life expectancy sample file as a fixture
    '''
    fixture_path = Path(__file__).parent / "fixtures" / "eu_life_expectancy_raw.tsv"
    return pd.read_csv(fixture_path, sep="\t")


@pytest.fixture
def expected_life_expectancy_eu_file():
    '''
    Defining the sample expected output file as a fixture
    '''
    fixture_path = Path(__file__).parent / "fixtures" / "eu_life_expectancy_expected.csv"
    return pd.read_csv(fixture_path)


@pytest.fixture(scope="session")
def pt_life_expectancy_expected() -> pd.DataFrame:
    """Fixture to load the expected output of the cleaning script"""
    return pd.read_csv(FIXTURES_DIR / "pt_life_expectancy_expected.csv")
