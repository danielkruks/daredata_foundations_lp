'''
This module contains the function that cleans the data.
'''
import pandas as pd

def clean_data(df: pd.DataFrame, region: str = None) -> pd.DataFrame:
    """Cleans the data from the life expectancy dataset. Optionally filters by region."""
    df[['unit', 'sex', 'age', 'geo']] = df.iloc[:, 0].str.split(',', expand=True)
    df = df.drop(columns=df.columns[0])
    df_melted = pd.melt(
        df,
        id_vars=['unit', 'sex', 'age', 'geo'],
        var_name='year',
        value_name='value'
    )
    df_melted.rename(columns={'geo': 'region'}, inplace=True)
    df_melted['year'] = df_melted['year'].astype(int)
    df_melted['value'] = pd.to_numeric(
                        df_melted['value'].str.replace(r'[^0-9.]','', regex=True), errors='coerce'
                        )
    if region is not None:
        df_melted = df_melted[(~df_melted['value'].isna()) & (df_melted['region'] == region)]
    return df_melted
