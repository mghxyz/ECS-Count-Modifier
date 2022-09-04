# ECS-Count-Modifier
Lambda code that can use with api-gateway or event-bridge to manually or automatically modify count of docker containers on Fargate or ECS.
Code written with python and boto3 for lambda function to modify number of fargate tasks automatically or manually.
You can use it with Api-Gateway or Eventbridge to schedule runnig docker container with change of desired number to any number more than zero.
and you can then turn them off with change desired number to zero.
You can specify more than one service with separating them with comma.
