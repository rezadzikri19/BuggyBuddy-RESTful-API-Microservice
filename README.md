# **REST API Microservice [BuggyBuddy🐞]**

## Overview

The **REST API Microservice [BuggyBuddy🐞]** plays a crucial role in the [BuggyBuddy](http://example.com) project, functioning as a RESTful API application designed to seamlessly integrate with various types of projects. Developed using FastAPI and seamlessly integrated with Swagger documentation, it provides a powerful and user-friendly interface for building and interacting with REST APIs.

## Features

- **RESTful API**:
  - Provides a comprehensive REST API interface for interacting with the BuggyBuddy system.
- **Integration with Pinecone Vector Database**:
  - Employs Pinecone for similarity searches on bug reports, aiding users in finding resolutions faster by suggesting similar resolved reports.
- **Built with FastAPI**:
  - Developed using FastAPI, a modern, high-performance web framework for building asynchronous Rest APIs with Python.

## Folder Structure
Utilizing clean architecture principles, this microservice offers seamless integration with different tech stacks. Simply switch drivers/implementation in the infrastructure for effortless adaptability.

```
my_project/
├── src/
│   └── core/
│       ├── dtos/         <- Data Transfer Objects (DTOs) for report CRUD operations and preprocessing.
│       ├── entities/     <- Entities representing report data.
│       ├── ports/        <- Ports defining contracts for message brokers, report CRUD operations, preprocessors, and vectorizers.
│       └── usecases/     <- Use cases for report CRUD operations and vectorization.
└── infrastructure/
    ├── api/              <- API routes (FastAPI), API DTOs (Pydantic).
    ├── main_drivers/     <- Main drivers for report CRUD operations (Pinecone), report preprocessing (Pandas, NumPy, and Sentence Transformers), and report vectorization (Keras and S3 with Boto3).
    ├── loggers/          <- Logger driver for capturing application logs.
    ├── message/          <- Message broker implementation (RabbitMQ with Pika).
    └── utils/            <- Common utility functions and helpers.

```

## Tech Stack

- **Programming Language**: Python
- **API Framework**: FastAPI
- **Data processing**: Pandas, Numpy
- **Model**: Tensorflow.Keras
- **Messaging**: RabbitMQ

## Installation

**1. Clone the repository:**

```bash
git clone <repository-url>
cd <repository-directory>
```

**2. Install & initialization:**

```bash
./entry_point.sh
```

**3. Configure the application environment:**

```bash
cp .env.example .env
```

> Edit the `.env` file and configure the necessary settings for your environment.

## Getting Started

To start using the BuggyBuddy REST API Microservice, follow the steps below:

1. Run the running script on your bash terminal:

```bash
./run.sh
```

2. Once the running is complete, you can interact with the system through the following endpoints:

- **GET /reports**: Retrieve details of a specific bug report by its ID.
- **GET /reports/similar**: Retrieve recommendations for similar bug reports based on the provided ID.
- **POST /reports**: Submit a new bug report to the system.
- **PUT /reports**: Submit a new bug report to the system.
- **DELETE /reports**: Submit a new bug report to the system.

The details can be found by accessing Swagger UI dashboard (**/docs**).

## Event Messaging

This microservice uses RabbitMQ event publised by the [ETL microservice]() which that inform new model is available then trigger new model loading from S3 Bucket. Below are *exchange*, *route*, and *data* of the subscribed message:

```bash
    exchange: 'train_service',
    routing_key: 'all_pipeline',
    data: {
      'status': 'SUCCESS' | 'FAILED',
      'message': 'TRAIN_PIPELINE [ALL] - SUCCESS' | <error_message>
    }
```

## License

This microservice is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute this software for any purpose, with or without attribution.
