# Hadoop MapReduce – Word Count Analysis

## Overview
This project demonstrates the core concepts of the Hadoop MapReduce programming model using a simple word count example.  
The implementation is written in Python to clearly illustrate how the Map and Reduce phases work on batch data.

The project focuses on understanding the logical flow of MapReduce rather than running on an actual Hadoop cluster.

---

## Objective
The objective of this project is to process a text input and calculate the frequency of each word by simulating:
- The Mapper phase
- The Shuffle and Sort phase (conceptual)
- The Reducer phase

---

## Project Structure
mapreduce-wordcount/
├── word_count.py
└── README.md


---

## How the Program Works

### 1. Input Handling
The program reads text data from standard input, which represents data stored in a distributed system such as HDFS.

Each line of text is treated as an independent input record.

---

### 2. Mapper Phase
The mapper function processes each line of text and emits intermediate key-value pairs.

- Each line is split into words
- Words are converted to lowercase
- Each word is mapped to the value `1`

Example output from the mapper:
(word, 1)


