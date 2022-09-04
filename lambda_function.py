import json
import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

client = boto3.client('ecs',region_name="ap-southeast-2")


def lambda_handler(event, context):
    if int(event["service_desired_count"]) >= 5 :
        service_desired_count = 5
    else:
        service_desired_count = int(event["service_desired_count"])
    
    cluster = event["cluster"]
    service_names = event["service_names"]
    for service_name in service_names.split(","):
        response = client.update_service(
            cluster=cluster,
            service=service_name,
            desiredCount=service_desired_count
        )

        logger.info(
            "Updated {0} service in {1} cluster with desire count set to {2} tasks".format(service_name, cluster,
                                                                                           service_desired_count))

    return {
    "statusCode": 200,
    "statusDescription": "200 OK",
    "isBase64Encoded": False,
    "headers": {
        "Content-Type": "text/html"
    },
    "body": "By MGH"
    }
    
