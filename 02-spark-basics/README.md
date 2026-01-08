# Data Analysis using Apache Spark (Spark SQL)

## Overview
This project focuses on performing structured data analysis using **Apache Spark SQL**.  
It demonstrates how to load data from a CSV file into a Spark DataFrame, apply schema definitions, and perform analytical queries using both the DataFrame API and Spark SQL.

The goal of this project is to strengthen understanding of Spark’s batch processing capabilities and SQL-based data analysis.

---

## Objective
To analyze employee data using Spark SQL by performing transformations, aggregations, filtering, and joins on structured datasets.

---

## Technologies Used
- Apache Spark (PySpark)
- Spark SQL
- Python
- CSV-based structured data

---

## Dataset
The dataset represents employee information and includes attributes such as:
- Employee Name
- Age
- Department
- Salary

The data is loaded from a CSV file and processed using Spark DataFrames.

---

## Tasks Performed

### Data Preparation
- Generated a Spark DataFrame from CSV data
- Defined an explicit schema for the dataset
- Displayed the schema to understand data structure

### SQL and DataFrame Operations
- Created a temporary view for SQL-based querying
- Executed SQL queries on the DataFrame
- Calculated average salary by department
- Filtered and displayed employees from the IT department
- Added a 10% bonus to employee salaries
- Found maximum salary based on age
- Performed a self-join on employee data
- Calculated average employee age
- Computed total salary by department
- Sorted employees by age and salary
- Counted employees in each department
- Filtered employees whose names contain the letter "o"

---

## Approach
1. Load CSV data into Spark using DataFrame reader
2. Apply schema definition for structured processing
3. Create a temporary SQL view
4. Perform analytical queries using Spark SQL
5. Apply transformations and aggregations using DataFrame operations
6. Display and analyze results

---

## Key Concepts Demonstrated
- SparkSession and DataFrame creation
- Schema definition and enforcement
- Temporary views and Spark SQL queries
- Data aggregation and grouping
- Filtering and sorting operations
- Join operations in Spark
- Batch data analysis using distributed processing

---

