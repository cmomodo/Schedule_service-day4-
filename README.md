# Schedule_service-day4-

## Sytem Design

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
  --template-file ecs.yaml \
  --stack-name sports-api-stack \
  --capabilities CAPABILITY_NAMED_IAM \
  --parameter-overrides \
    VpcId=vpc-
vpc-007940c16331d8332 \
    SubnetIds=subnet-subnet-007e23dbf72eda1d1,subnet-086c08f155e218774
```
