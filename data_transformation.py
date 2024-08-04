import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

def transform_data(data):
    # Handle missing values
    data['Age'].fillna(data['Age'].median(), inplace=True)
    data['Embarked'].fillna(data['Embarked'].mode()[0], inplace=True)
    data.drop(columns=['Cabin'], inplace=True)

    # Feature engineering
    data['Title'] = data['Name'].apply(lambda x: x.split(',')[1].split('.')[0].strip())
    data['FamilySize'] = data['SibSp'] + data['Parch'] + 1

    # Select numerical and categorical columns
    numerical_cols = ['Age', 'Fare', 'FamilySize']
    categorical_cols = ['Sex', 'Embarked', 'Title']
    target_col = 'Survived'

    # Define the transformers
    numerical_transformer = StandardScaler()
    categorical_transformer = OneHotEncoder(handle_unknown='ignore')

    # Create a column transformer
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numerical_transformer, numerical_cols),
            ('cat', categorical_transformer, categorical_cols)
        ]
    )

    # Apply the transformations
    data_transformed = preprocessor.fit_transform(data)

    # Convert the transformed data back to a DataFrame for convenience
    transformed_columns = numerical_cols + list(preprocessor.named_transformers_['cat'].get_feature_names_out(categorical_cols))
    data_transformed_df = pd.DataFrame(data_transformed.toarray(), columns=transformed_columns)
    
    # Add the target column back to the DataFrame
    data_transformed_df[target_col] = data[target_col].values
    
    return data_transformed_df

if __name__ == "__main__":
    data = pd.read_csv('train.csv')
    data_transformed = transform_data(data)
    print(data_transformed.head())
