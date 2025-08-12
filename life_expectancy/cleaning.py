'''This script creates a function to clean life expectancy data
and filter based on country preference, subsetting a .csv file output'''

import argparse
import pandas as pd


# Breaking down the original function into three splits (assignment2)
def load_data(data_path: str) -> pd.DataFrame:
    """Loads the life expectancy data."""
    if data_path.endswith(".tsv"):
        lfex_data = pd.read_csv(data_path, sep='\t')
    else:
        raise ValueError("Unsupported file format")
    return lfex_data


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Cleans the data from the life expectancy dataset."""
    # Splitting the first column into multiple columns (2.ii.)
    df[['unit', 'sex', 'age', 'geo']] = df.iloc[:, 0].str.split(',', expand=True)

    df = df.drop(columns=df.columns[0])

    df_melted = pd.melt(
        df,
        id_vars=['unit', 'sex', 'age', 'geo'],
        var_name='year',
        value_name='value'
    )

    df_melted.rename(columns={'geo': 'region'}, inplace=True)

    # Converting 'year' to integer and 'value' to numeric
    # handling non-numeric values (2.iii. & 2.iv.)
    df_melted['year'] = df_melted['year'].astype(int)


    df_melted['value'] = pd.to_numeric(df_melted['value'].str.replace(
                                        r'[^0-9.]','', regex=True), errors='coerce')

    return df_melted


def save_data(df: pd.DataFrame, country: str):
    """Saves the cleaned data to a CSV file, for a specific country."""
    # Subsetting the data for non-null values and the specified country (2.v.)
    country_data = df[(~df['value'].isna()) & (df['region'] == country)]

    country_data.to_csv(f'./life_expectancy/data/{country.lower()}_life_expectancy.csv',
                        index=False)


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
    df_clean = clean_data(df)
    save_data(df_clean, args.country)

if __name__ == "__main__":  # pragma: no cover
    main()
