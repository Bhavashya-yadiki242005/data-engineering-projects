# Graph Processing using GraphFrames in PySpark

## Overview
This project demonstrates graph-based data processing using the **GraphFrames** library in Apache Spark.
It focuses on modeling relationships between entities as a graph and performing common graph analytics
using Spark’s distributed processing capabilities.

The project was implemented to understand how graph data can be represented and analyzed using Spark
beyond traditional tabular data processing.

---

## Objective
To explore graph analytics using PySpark by creating a graph structure and performing fundamental
graph operations such as degree analysis, breadth-first search, and connected components.

---

## Technologies Used
- Apache Spark (PySpark)
- GraphFrames
- Python

---

## Graph Model

### Vertices (Nodes)
Vertices represent entities in the graph and include attributes such as:
- Unique ID
- Name

### Edges (Relationships)
Edges represent relationships between vertices and include:
- Source node
- Destination node
- Relationship type

---

## Operations Performed

### Graph Creation
- Created vertices and edges as Spark DataFrames
- Constructed a GraphFrame using the vertex and edge DataFrames

### Degree Analysis
- Calculated in-degrees for each vertex
- Calculated out-degrees for each vertex
- Calculated total degrees

### Graph Traversal
- Performed **Breadth First Search (BFS)** to find paths between two nodes

### Graph Connectivity
- Identified **connected components** to group related vertices

---
graphframes-example/
├── graphframes_example.py
└── README.md

## Key Concepts Demonstrated
- Graph modeling using Spark DataFrames
- GraphFrames API usage
- Degree calculations in graphs
- Graph traversal using BFS
- Connected components analysis
- Batch graph processing in Spark

## Project Structure

