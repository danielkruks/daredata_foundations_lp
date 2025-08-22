'''This script creates a function to clean life expectancy data
and filter based on country preference, subsetting a .csv file output'''

import argparse
from life_expectancy.loader import load_data
from life_expectancy.cleaner import clean_data
from life_expectancy.saver import save_data

def main():
    """Main function to execute the cleaning process."""
    parser = argparse.ArgumentParser(description="Clean life expectancy data for a given country.")
    parser.add_argument(
        "--country",
        type=str,
        default="PT",
        help="Country code to filter (default: PT)"
    )
    parser.add_argument(
        "--data-path",
        type=str,
        default="./life_expectancy/data/eu_life_expectancy_raw.tsv",
        help="Path to the raw data file"
    )
    args = parser.parse_args()
    df = load_data(args.data_path)
    df_clean = clean_data(df, region=args.country)
    save_data(df_clean)
    return df_clean

if __name__ == "__main__":  # pragma: no cover
    main()
