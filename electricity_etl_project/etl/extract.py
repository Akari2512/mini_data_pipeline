import pandas as pd

def extract_from_csv(file_path: str) -> pd.DataFrame:
    """
    Extracts data from a CSV file and returns it as a pandas DataFrame.
    """
    try:
        df = pd.read_csv(file_path)
        print(f'[INFO] Data extracted successfully from {file_path}')
        print(f'[INFO] Data rows: {df.shape[0]}, Data columns: {df.shape[1]}' )
        return df
    except Exception as e:
        print(f'[ERROR] Failed to extract data from {file_path}: {e}')
        return pd.DataFrame()