# **🧭 BuggyBuddy REST API [Microservice]**

## Overview

The **BuggyBuddy REST API Microservice** plays a crucial role in the [BuggyBuddy](http://example.com) project, functioning as a RESTful API application designed to seamlessly integrate with various types of projects. Developed using FastAPI and integrated with Swagger documentation, it provides a powerful and user-friendly interface for building and interacting with REST APIs.

## Features

- **Integration with Pinecone Vector Database**:
  - Menggunakan Pinecone vector database, allowing for fast and scalable application.
- **Built with FastAPI**:
  - Developed using FastAPI, a modern, high-performance web framework for building asynchronous Rest APIs with Python.
- **Swagger Documentation**:
  - built-in Swagger documentation, simplifying interfacing with other applications.


## Folder Structure
Utilizing clean architecture principles, this microservice provides effortless integration with various technology stacks. You can easily switch drivers or implementations within the infrastructure, ensuring smooth adaptability.

```
my_project/
├── src/
│   └── core/
│       ├── dtos/         <- DTOs for transferring data between pipelines/modules.
│       ├── entities/     <- Domain entities representing data objects.
│       ├── ports/        <- Ports defining contracts for drivers.
│       └── usecases/     <- Use cases implementing business logic.
└── infrastructure/
    ├── api/              <- API routes and DTOs.
    ├── main_drivers/     <- Data and CRUD drivers.
    ├── loggers/          <- Logging utilities drivers.
    ├── message/          <- Message broker drivers (RabbitMQ).
    └── utils/            <- Additional utilities and helpers for infrastructure-related tasks.

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

- **GET /reports**: Retrieve bug reports by specific filters such id, component, platform, etc. (*require req. body*).
- **GET /reports/similar**: Retrieve 10 most similar bug reports (*require req. body*).
- **POST /reports**: Create a new bug report (*require req. body*).
- **PUT /reports/{report_id}**: Update a bug report (*require req. body*).
- **DELETE /reports/{report_id}**: Delete a bug report.

The details can be found by accessing Swagger UI dashboard (**/docs**).

## Event Messaging

This microservice subscribes to RabbitMQ events published by the [BuggyBuddy Model Builder Microservice](https://github.com/uknow19/BuggyBuddy-Model-Builder-Microservice). These events inform when a new model is available, triggering the loading of the new model from the S3 Bucket. Below are the *exchange*, *route*, and *data* of the subscribed message.

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
