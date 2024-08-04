
import pandas as pd

def extract_data(filepath):
    data = pd.read_csv(filepath)
    return data

if __name__ == "__main__":
    data = extract_data('train.csv')
    print(data.head())
        