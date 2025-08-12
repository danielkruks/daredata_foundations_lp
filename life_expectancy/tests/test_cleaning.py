"""Tests for the cleaning module"""
import pandas as pd
from life_expectancy.cleaning import load_data, clean_data, save_data
from . import OUTPUT_DIR

def test_clean_data(pt_life_expectancy_expected):
    """Test the cleaning of life expectancy data for Portugal."""
    # Testing function no.1
    df = load_data(str(OUTPUT_DIR.parent / "data" / "eu_life_expectancy_raw.tsv"))
    # Testing function no.2
    df_clean = clean_data(df)
    # Testing function no.3
    save_data(df_clean, "PT")
    pt_life_expectancy_actual = pd.read_csv(OUTPUT_DIR / "pt_life_expectancy.csv")
    pd.testing.assert_frame_equal(
        pt_life_expectancy_actual, pt_life_expectancy_expected
    )
