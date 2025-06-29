import pandas as pd
import numpy as np

def transform_data(df:pd.DataFrame) -> pd.DataFrame:
    """
    Transforms the input DataFrame by cleaning and processing the data.
    """

    # Replacing 0 with NaN for specific columns
    df['num_people'] = df['num_people'].replace(0, np.nan)
    df['num_rooms'] = df['num_rooms'].replace(0, np.nan)
    df.loc[df['num_people'] < 0, 'num_people'] = np.nan
    

    # Dealing with missing values
    df['invalid_data'] = df[['num_people', 'num_rooms', 'housearea']].isnull().any(axis=1)
    
    # Creating new features
    valid_df = df[~df['invalid_data']].copy()
    valid_df.drop(columns=['invalid_data'], inplace=True)
    valid_df['bill_per_person'] = valid_df['amount_paid'] / valid_df['num_people']
    valid_df['bil_per_sqft'] = valid_df['amount_paid'] / valid_df['housearea']
    valid_df['room_density'] = valid_df['num_people'] / valid_df['num_rooms']

    print(f'[INFO] Data transformed succeessfully')
    print(f'[INFO] Valid data: {valid_df.shape}')

    return valid_df



