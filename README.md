# Collector API

A FastAPI-based service for collecting, transforming, and processing event data using Kafka for messaging.

## Overview

This project implements a data collection API that:
1. Receives event data through a RESTful API endpoint
2. Publishes the raw data to a Kafka topic
3. Consumes, transforms, and republishes the data to another Kafka topic

## Architecture

```
Client -> FastAPI Endpoint (/collect) -> Kafka Topic (collect-topic1) -> Consumer -> Kafka Topic (collect-topic2)
```

### Components

- **FastAPI Server** (`main.py`): Provides the API endpoints
- **Data Collection** (`collect.py`): Handles the incoming data and publishes to Kafka
- **Data Models** (`models.py`): Defines the data structures using Pydantic
- **Consumer** (`consumer.py`): Processes messages from Kafka, transforms data, and republishes

## Installation

1. Clone the repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Ensure Kafka is running on `localhost:9092`

## Usage

### Starting the API Server

```bash
uvicorn main:app --reload
```

The server will start at http://localhost:8000 by default.

### API Endpoints

- `GET /`: Home page
- `POST /collect`: Submit event data

### Sample Request

Send a POST request to `/collect` with a JSON body like:

```json
{
  "events": [
    {
      "event_type": "product_view",
      "event_time": 1750867000000,
      "user_id": "user_test",
      "product_id": "prod_demo"
    }
  ],
  "ctx": {
    "browser": "Firefox",
    "device": "Desktop",
    "version": "126.0"
  }
}
```

### Running the Consumer

Start the consumer to process messages from Kafka:

```bash
python consumer.py
```

## Dependencies

- FastAPI
- Pydantic
- Kafka Python
- Uvicorn

## Development

The project requires a running Kafka instance. Make sure you have Kafka set up and running on `localhost:9092` before starting the application.

## Data Flow

1. Client submits event data to the `/collect` endpoint
2. The API publishes the raw data to `collect-topic1` Kafka topic
3. The consumer reads from `collect-topic1`, transforms the data, and publishes to `collect-topic2`
