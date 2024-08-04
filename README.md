
# ETL and ML Pipeline for Titanic Dataset

## Overview

This project demonstrates the ETL process and integration with a simple ML pipeline using the Titanic dataset from Kaggle.

## Files

- `data_extraction.py`: Script for data extraction.
- `data_transformation.py`: Script for data transformation.
- `data_loading.py`: Script for data loading.
- `ml_pipeline.py`: Script for ML pipeline integration.
- `README.md`: Instructions on how to run the scripts and set up the environment.

## Setup

1. Ensure you have Python installed (preferably Python 3.8 or later).
2. Install the required libraries:

```sh
pip install pandas scikit-learn sqlalchemy
```

## Instructions

1. **Data Extraction**:
   Run the data extraction script to extract data from the CSV file:
   ```sh
   python data_extraction.py
   ```

2. **Data Transformation**:
   Run the data transformation script to clean and preprocess the data:
   ```sh
   python data_transformation.py
   ```

3. **Data Loading**:
   Run the data loading script to load the transformed data into the SQLite database:
   ```sh
   python data_loading.py
   ```

4. **ML Pipeline**:
   Run the ML pipeline script to train and evaluate the model:
   ```sh
   python ml_pipeline.py
   ```

## Dataset

This dataset contains information about the passengers aboard the Titanic and is commonly used for introductory ML tasks.

https://www.kaggle.com/competitions/titanic/data

### Group Members:

- Piyush Borse
- Bhawana Gurumukhdas Thawarani
- Yuvraj Singh Srinet 
- Prateek Majumder
- Neha Roy Choudhury
- Prajwal Wagh

        
