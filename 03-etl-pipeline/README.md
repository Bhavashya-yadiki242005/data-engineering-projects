# Python ETL Pipeline – API to CSV

## Overview
This project demonstrates a simple yet complete **ETL (Extract, Transform, Load)** pipeline implemented using Python.  
The objective of the project is to fetch data from a public REST API, apply meaningful transformations, and store the processed data in a structured CSV format.

The project is designed to reflect real-world data engineering fundamentals such as API handling, data cleaning, transformation logic, and modular code structure.

---

## Problem Statement
In many data engineering scenarios, raw data is obtained from external APIs in JSON format.  
This data is often not directly usable and requires cleaning, filtering, and enrichment before it can be stored or analyzed.

This project solves the problem by:
- Extracting raw JSON data from an API
- Transforming it into a structured and enriched format
- Loading the final output into a CSV file for further analysis or reporting

---

## Tools & Technologies Used
- **Python** – Core programming language  
- **Pandas** – Data manipulation and transformation  
- **Requests** – Handling REST API calls  
- **REST API** – JSONPlaceholder public API  

---

## Data Source
The data is fetched from the following public API:
https://jsonplaceholder.typicode.com/posts


This API provides sample post data in JSON format and is commonly used for testing and learning purposes.

---

## ETL Process Explanation

### 1. Extract
The extraction phase involves making an HTTP GET request to the API endpoint using the `requests` library.  
The response is received in JSON format and converted into a Python object for further processing.

**Key points:**
- API call is handled inside a dedicated function
- JSON response is parsed safely
- Raw data remains unchanged at this stage

---

### 2. Transform
The transformation phase focuses on converting raw data into meaningful, structured information using Pandas.

The following transformations are applied:
- JSON data is converted into a Pandas DataFrame
- Records are filtered where `userId` is less than or equal to 5
- A new column `title_length` is created to store the length of each title
- Title text is cleaned and formatted by capitalizing each word
- A new column `summary` is created using the first 50 characters of the body text

These transformations simulate real-world data cleaning and enrichment tasks commonly performed in ETL pipelines.

---

### 3. Load
In the loading phase, the transformed DataFrame is written to a CSV file.  
This represents storing processed data in a structured format that can be easily consumed by analysts, reporting tools, or downstream systems.

The CSV file is saved without an index to maintain clean formatting.

---

## Project Structure
python-etl-api-to-csv/
│
├── etl.py
├── enhanced_etl_output.csv
├── requirements.txt
└── README.md


---

## How to Run the Project

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt

### Step 1: Install Dependencies
run:
  step: "Run the ETL Script"
  command: "python etl.py"
  output_file: "enhanced_etl_output.csv"

step_2:
  run_etl_script:
    command: python etl.py
    output_file: enhanced_etl_output.csv

output:
  description: Output CSV file details
  contents:
    - Filtered user records
    - Enriched metadata such as title length
    - Cleaned and formatted text fields
    - Short summaries for each record

Output

The output CSV file contains:

Filtered user records

Enriched metadata such as title length

Cleaned and formatted text fields

Short summaries for each record



