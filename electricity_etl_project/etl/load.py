def load_to_sql(df, engine, table_name='electricity_bills'):
    """
    Loads the DataFrame to a SQL database table.
    """
    try:
        df.to_sql(name=table_name, con=engine, if_exists='append', index=False)
        print(f'[INFO] Successfully loaded {len(df)} rows to {table_name} table.')
    except Exception as e:
        print(f'[ERROR] Failed to load data to {table_name} table: {e}')