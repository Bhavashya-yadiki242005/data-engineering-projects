# Movie Ratings Analysis using Hive SQL

## Overview
This project demonstrates a basic **data lake–style analysis** using **Hive SQL** on raw movie ratings data.
The objective is to load semi-structured data into Hive, apply a schema at query time, and perform analytical queries.

The project is executed in a **Hortonworks Sandbox** environment, which simulates a real Hadoop ecosystem commonly used in data engineering workflows.

---

## Why This Project
In real-world data engineering systems, data often arrives as raw files and is stored first before being structured.
This project follows that principle by:

- Working with raw data files
- Applying schema using Hive (**schema-on-read**)
- Running analytical SQL queries on top of the data

This approach aligns closely with **data lake fundamentals**.

---

## Technologies Used
- Hive SQL
- Hadoop (HDFS / local sandbox storage)
- Hortonworks Sandbox
- Linux (PuTTY terminal)

---

## Data Description
The dataset contains movie ratings data with the following fields:

- `user_id` – ID of the user  
- `movie_id` – ID of the movie  
- `rating` – Rating given by the user  
- `timestamp` – Time of rating  

The data is stored as a raw `.data` file and loaded into Hive for analysis.

---

## Project Workflow
1. Drop the existing database if it already exists
2. Create a new database
3. Create a Hive table with an appropriate schema
4. Load raw data into the table
5. Run analytical queries to explore the data

This workflow represents a **batch data processing pipeline** over data lake storage.

---

## Hive SQL Code

```sql
-- Drop existing database
DROP DATABASE IF EXISTS movies CASCADE;

-- Create new database
CREATE DATABASE IF NOT EXISTS movies;

-- Use the database
USE movies;

-- Create Ratings table
CREATE TABLE Ratings (
    user_id INT,
    movie_id INT,
    rating INT,
    timestamp INT
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t'
LINES TERMINATED BY '\n'
STORED AS TEXTFILE;

-- Load data from local file into Hive table
LOAD DATA LOCAL INPATH '/home/maria_dev/ratings.data'
INTO TABLE Ratings;

-- Get metadata of the table
DESCRIBE Ratings;

-- Get total number of records
SELECT COUNT(*) FROM Ratings;

-- Get number of occurrences for each rating
SELECT
    rating,
    COUNT(rating) AS total_occurrences
FROM Ratings
GROUP BY rating
ORDER BY total_occurrences DESC;

How to Run the Project
Step 1: Start Hortonworks Sandbox

Start the VM using VMware or VirtualBox

Ensure all required services are running

Step 2: Login via PuTTY

Connect to the sandbox IP

Login credentials:

Username: maria_dev

Password: maria_dev

Step 3: Start Hive
hive

Step 4: Run the SQL Script
SOURCE /home/maria_dev/movieratings.sql;

Output

The queries provide:

Total number of ratings

Distribution of ratings (from most common to least common)
