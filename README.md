# Schedule_service-day4-

## System Design

![System Design Diagram](/images/live_schedule_api.png)

## Services used

- Docker
- Flask
- ECR
- ECS
- API Gateway

## Steps to run the project

- Clone the repository
- Run the following commands

```
aws cloudformation deploy \
  --template-file grok.yaml \
  --stack-name sports-api-stack \
  --capabilities CAPABILITY_NAMED_IAM
```
