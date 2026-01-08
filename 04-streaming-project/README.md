# Spark Structured Streaming – Socket Word Count

## Overview
This project demonstrates a real-time word count application using **Apache Spark Structured Streaming**.
It processes streaming text data received from a socket source and continuously computes word frequencies.

The project was implemented to understand Spark’s streaming architecture, micro-batch processing model, and stateful aggregations.

---

## Objective
To process incoming streaming data in real time and calculate the frequency of each word as data arrives continuously.

---

## Technologies Used
- Apache Spark (PySpark)
- Spark Structured Streaming
- Python
- Socket-based streaming source

---

## Data Source
- Streaming text input from a local socket
- Host: `localhost`
- Port: `9999`

---
04-streaming-project/
├── socket_word_count.py
└── README.md


---

## How the Program Works

### 1. Spark Session Creation
A Spark session is created as the entry point for Structured Streaming operations.

---

### 2. Reading Streaming Data
Streaming data is read from a socket source using Spark’s `readStream` API.
Each line of text received from the socket is treated as a streaming record.

---

### 3. Data Transformation
- Incoming lines are split into individual words
- Words are flattened using the `explode` function
- Each word is grouped and counted in real time

---

### 4. Streaming Aggregation
Word counts are continuously updated using Spark’s stateful aggregation mechanism.

---

### 5. Output and Checkpointing
- Aggregated results are written to the console
- Checkpointing is enabled to maintain fault tolerance and streaming state

---

## How to Run the Project

### Step 1: Start Socket Server
Run the following command in a terminal:
nc -lk 9999

Type words or sentences and press Enter to send streaming data.

---

### Step 2: Run the Spark Application
Execute the `socket_word_count.py` file using Spark.

The application will display updated word counts on the console every few seconds.

---

## Example

### Input (Streaming)
spark streaming is powerful
spark streaming is fast

### Output
spark 2
streaming 2
is 2
powerful 1
fast 1
## Project Structure

