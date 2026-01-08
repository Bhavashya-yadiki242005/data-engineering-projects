# Kafka Producer–Consumer (Learning Project)

## Overview
This project demonstrates the basic working of an **Apache Kafka Producer and Consumer** using **Java 8**.
It focuses on understanding how messages are produced to Kafka topics and consumed by consumers using Kafka’s
publish–subscribe messaging model.

This project is included as part of my **data engineering learning journey** to understand event-driven
data pipelines and messaging systems.

---

## Objective
To learn the fundamentals of Apache Kafka, including:
- Setting up Kafka and Zookeeper
- Creating Kafka topics
- Producing messages to Kafka topics
- Consuming messages from Kafka topics
- Understanding partitions and message flow

---

## Technologies Used
- Apache Kafka
- Apache Zookeeper
- Java 8
- Kafka Producer and Consumer APIs

---

## Prerequisites
Before running this project, ensure the following are available:
- Java 8 installed
- Apache Kafka downloaded
- Apache Zookeeper configured

---

## Kafka Setup

### Start Zookeeper
Zookeeper is required for Kafka to manage configurations and metadata.

```bash
zookeeper-server-start.bat config/zookeeper.properties

Default port: 2181
Start Kafka Broker

Start Kafka using the server configuration file
kafka-server-start.bat config/server.properties
kafka-server-start.bat config/server.properties
Default port: 9092


Application Workflow

Create a Kafka topic
Configure the Kafka Producer with:
bootstrapServerHost = "127.0.0.1:9092";
Create producer records using:
ProducerRecord<String, String>
Records with the same key are sent to the same partition.
Configure the Kafka Consumer with the same bootstrap server
Subscribe the consumer to the topic
Run the producer application to publish messages
Run the consumer application to consume messages from the topic
