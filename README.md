# MLOps-Project

## Instructions

### 1. Setting Up and Running the Pipeline

#### 1.1 Prerequisites
- Docker installed on your machine.
- Google Cloud SDK installed and configured.

#### 1.2 Cloning the Repository
```bash
git clone https://github.com/m-mahmoud-mohamed/MLOps-Pipeline-for-Machine-Learning-Deployment.git
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

#### 2.3 Using vertex API

This screenshot shows a Python script interfacing with a Google Vertex AI endpoint to make a prediction. The script initializes the endpoint, prepares the input data, and sends a prediction request. The response, which classifies the input as 'Trojan,' is then printed, demonstrating the model's deployment and usage in a production environment.

![image](https://github.com/m-mahmoud-mohamed/MLOps-Project/assets/78882792/24144d80-b1e5-41ef-a9e0-78980f43db78)






