import pandas as pd

def load_data(data_path: str) -> pd.DataFrame:
    """Loads the life expectancy data from a TSV file."""
    if data_path.endswith(".tsv"):
        lfex_data = pd.read_csv(data_path, sep='\t')
    else:
        raise ValueError("Unsupported file format")
    return lfex_data
