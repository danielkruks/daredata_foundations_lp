'''This script creates a function to clean life expectancy data
and filter based on country preference, subsetting a .csv file output'''

import argparse
import pandas as pd

def clean_data(country: str = 'PT'):
    '''Function to clean life expectancy data and filter for Portugal'''
    # 2.i.
    lfex = pd.read_csv('./life_expectancy/data/eu_life_expectancy_raw.tsv', sep='\t')

    # 2.ii.
    lfex[['unit', 'sex', 'age', 'geo']] = lfex.iloc[:, 0].str.split(',', expand=True)

    lfex = lfex.drop(columns=lfex.columns[0])

    lfex_melted = pd.melt(
        lfex,
        id_vars=['unit', 'sex', 'age', 'geo'],
        var_name='year',
        value_name='value'
    )

    lfex_melted.rename(columns={'geo': 'region'}, inplace=True)

    # 2.iii.
    lfex_melted['year'] = lfex_melted['year'].astype(int)

    # 2.iv.
    lfex_melted['value'] = pd.to_numeric(lfex_melted['value'].str.replace(
                                        r'[^0-9.]','', regex=True), errors='coerce')

    # 2.v.
    pt_lfex = lfex_melted[(~lfex_melted['value'].isna()) & (lfex_melted['region'] == country)]


    # 2.vi.
    pt_lfex.reset_index(drop=True, inplace=True)
    pt_lfex.to_csv('./life_expectancy/data/pt_life_expectancy.csv', index=False)

if __name__ == "__main__": #pragma: no cover
    parser = argparse.ArgumentParser(description="Clean life expectancy data for a given country.")
    parser.add_argument(
        "--country",
        type=str,
        default="PT",
        help="Country code to filter (default: PT)"
    )
    args = parser.parse_args()
    clean_data(args.country)
