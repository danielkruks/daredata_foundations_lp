'''
This file was used to create the sample of data requested in assignment 3
'''

from pathlib import Path
import pandas as pd
from life_expectancy.main import load_data, clean_data, save_data


# Paths
full_data_path = (Path(__file__).parents[2]
                  / "life_expectancy"
                  / "data"
                  / "eu_life_expectancy_raw.tsv"
)

fixtures_dir = Path(__file__).parent / "fixtures"
fixtures_dir.mkdir(parents=True, exist_ok=True)
fixture_path = fixtures_dir / "eu_life_expectancy_raw.tsv"

# Load the full dataset
df = pd.read_csv(str(full_data_path), sep="\t")
# Select 5 rows where the first column contains 'PT'
first_col = df.columns[0]
pt_rows = df[df[first_col].str.contains(',PT', regex=False)].sample(n=5, random_state=42)
# Select 7 rows that do NOT contain 'PT'
other_rows = df[~df[first_col].str.contains(',PT', regex=False)].sample(n=7, random_state=42)
# Combine and shuffle the sample
sample = pd.concat([pt_rows, other_rows]).sample(frac=1, random_state=42)
# Save the sample to the fixture file
sample.to_csv(fixture_path, sep="\t", index=False)
print(f"Sample fixture created at: {fixture_path.resolve()}")

# Creating the expected output fixture
df_sample = load_data(str(fixture_path))
df_cleaned = clean_data(df_sample, region='PT')
save_data(df_cleaned, fixtures_dir, 'eu_life_expectancy_expected.csv')
print(f"Expected output fixture created at: {fixtures_dir.resolve()}")