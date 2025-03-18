# NFL Schedule API Service

A robust AWS-based microservice that provides NFL schedule information through a RESTful API.

## System Design

![System Design Diagram](/images/live_schedule_api.png)

## Features

- Fetches real-time NFL schedule data from SerpAPI
- Serverless architecture using AWS Fargate (no server management)
- Highly available with multi-AZ deployment
- Auto-scaling capabilities to handle varying loads
- CORS support for browser-based requests
- Comprehensive logging and monitoring

## AWS Services Used

- **Docker**: Containerization of the Flask application
- **Amazon ECR**: Container registry for storing Docker images
- **Amazon ECS with Fargate**: Serverless compute engine for containers
- **Application Load Balancer**: For distributing traffic and health checks
- **Amazon API Gateway**: API management with CORS support
- **Amazon CloudWatch**: Logging and monitoring
- **AWS CloudFormation**: Infrastructure as Code (IaC)

## API Endpoints

- `GET /sports`: Returns current NFL schedule information
- Response format:
  ```json
  {
    "message": "NFL schedule fetched successfully.",
    "games": [
      {
        "away_team": "Team A",
        "home_team": "Team B",
        "venue": "Stadium Name",
        "date": "Date of game",
        "time": "Time of game ET"
      }
      // More games...
    ]
  }
  ```

## Prerequisites

- AWS CLI installed and configured
- Docker installed (for local development)
- SerpAPI API key (stored in .env file)

## Deployment

Deploy the entire stack using AWS CloudFormation:

```bash
aws cloudformation deploy \
  --template-file ecs.yaml \
  --stack-name sports-api-stack \
  --capabilities CAPABILITY_NAMED_IAM
```

## Deactivating Resources

To clean up all resources:

```bash
./deactivate.sh
```

## Local Development

1. Create a `.env` file with your SerpAPI key:
   ```
   SPORTS_API_KEY=your_serp_api_key
   ```

2. Build and run the Docker container:
   ```bash
   docker build -t sports-api .
   docker run -p 8080:8080 --env-file .env sports-api
   ```

3. Test the API locally:
   ```bash
   curl http://localhost:8080/sports
   ```

## Security Considerations

- API Gateway configured with proper request throttling
- Network security groups restrict traffic to required ports only
- Secrets management via environment variables
- Least privilege IAM roles