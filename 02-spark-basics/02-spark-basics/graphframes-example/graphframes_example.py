from pyspark.sql import SparkSession
from graphframes import GraphFrame

def main():
    # 1. Create Spark Session
    spark = SparkSession.builder \
        .appName("GraphFramesExample") \
        .getOrCreate()

    spark.sparkContext.setLogLevel("ERROR")

    # 2. Create Vertices (Nodes)
    vertices = spark.createDataFrame([
        ("1", "Alice"),
        ("2", "Bob"),
        ("3", "Charlie")
    ], ["id", "name"])

    # 3. Create Edges (Relationships)
    edges = spark.createDataFrame([
        ("1", "2", "friend"),
        ("2", "3", "follow"),
        ("3", "2", "follow")
    ], ["src", "dst", "relationship"])

    # 4. Create Graph
    graph = GraphFrame(vertices, edges)

    # 5. Display Vertices and Edges
    print("Vertices:")
    graph.vertices.show()

    print("Edges:")
    graph.edges.show()

    # 6. Graph Operations

    # In-Degree
    print("In-Degrees:")
    graph.inDegrees.show()

    # Out-Degree
    print("Out-Degrees:")
    graph.outDegrees.show()

    # Total Degree
    print("Total Degrees:")
    graph.degrees.show()

    # 7. Breadth First Search (BFS)
    print("Breadth First Search from Alice to Charlie:")
    bfs_result = graph.bfs(
        fromExpr="name = 'Alice'",
        toExpr="name = 'Charlie'",
        maxPathLength=3
    )
    bfs_result.show()

    # 8. Connected Components
    print("Connected Components:")
    components = graph.connectedComponents()
    components.show()

    # Stop Spark
    spark.stop()

if __name__ == "__main__":
    main()
