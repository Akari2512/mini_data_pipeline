from etl.extract import extract_from_csv
from etl.transform import transform_data
from etl.load import load_to_sql
from utils.db_connection import get_engine

if __name__ == '__main__':
    file_path = 'data/Household energy bill data.csv'
    df = extract_from_csv(file_path)

    df_transformed = transform_data(df)

    engine = get_engine()
    load_to_sql(df_transformed, engine)
    