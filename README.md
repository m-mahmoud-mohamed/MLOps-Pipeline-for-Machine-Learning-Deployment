# MLOps-Project

## Instructions

### 1. Setting Up and Running the Pipeline

#### 1.1 Prerequisites
- Docker installed on your machine.
- Google Cloud SDK installed and configured.

#### 1.2 Cloning the Repository
```bash
git clone [https://github.com/m-mahmoud-mohamed/MLOps-Project](https://github.com/m-mahmoud-mohamed/MLOps-Project.git)
```
```bash
cd <repository-directory>
```

#### 1.3 Building the Docker Image

```bash
docker build -t image_name .
```

#### 1.4 Running the Docker Container

```bash
docker run -p 5000:5000 image_name
```
### 2. Using the API

#### 2.1 API Endpoints
GET /: Returns a welcome message.
POST /predict: Accepts JSON payload with input features and returns prediction.

#### 2.2 Example Requests and Responses

Example Request:

```bash
curl -X POST http://localhost:5000/predict -H "Content-Type: application/json" -d '{
  "features": [value1, value2, ..., value450]
}'
```

Example Response:

```bash
{
  "prediction": "label"
}
```





