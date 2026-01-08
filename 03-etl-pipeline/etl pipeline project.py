import requests
import pandas as pd

def extract_data(api_url):
    response = requests.get(api_url)
    data = response.json()
    return data

def transform_data(data):
    # Convert JSON data to a Pandas DataFrame
    df = pd.DataFrame(data)

    # Step 1: Filter records where userId is less than or equal to 5
    df = df[df['userId'] <= 5]

    # Step 2: Add a new computed column 'title_length' which is the length of title
    df['title_length'] = df['title'].apply(len)

    # Step 3: Clean and format the 'title' column to capitalize each word
    df['title'] = df['title'].str.title()

    # Step 4: Add a new column 'summary' which is the first 50 characters of body
    df['summary'] = df['body'].apply(lambda x: x[:50] + '...')

    return df

def load_data(df, file_name):
    # Save DataFrame to a CSV file
    df.to_csv(file_name, index=False)

def etl_process():
    api_url = "https://jsonplaceholder.typicode.com/posts"  # Sample API URL
    file_name = "enhanced_etl_output.csv"  # Output CSV file name

    # Step 1: Extract
    data = extract_data(api_url)

    # Step 2: Transform
    df = transform_data(data)

    # Step 3: Load
    load_data(df, file_name)

    print("Data has been successfully extracted, transformed, and loaded into CSV file.")

# Run ETL process
etl_process()
