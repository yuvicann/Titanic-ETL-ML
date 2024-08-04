import pandas as pd
from sqlalchemy import create_engine
from data_transformation import transform_data

def load_data_to_db(data, db_name='sqlite:///titanic.db'):
    engine = create_engine(db_name)
    data.to_sql('titanic_transformed', engine, index=False, if_exists='replace')

def load_data_from_db(db_name='sqlite:///titanic.db'):
    engine = create_engine(db_name)
    query = "SELECT * FROM titanic_transformed"
    data_from_db = pd.read_sql(query, engine)
    return data_from_db

if __name__ == "__main__":
    # Extract data
    data = pd.read_csv('train.csv')
    # Transform data
    transformed_data = transform_data(data)
    # Load data into the database
    load_data_to_db(transformed_data)
    # Verify data loading
    data_loaded = load_data_from_db()
    print(data_loaded.head())
