import json
import main

def hello(event, context):
    body = json.loads(event['body'])

    returnBody = {
        "country": main.determineChoice(body['questions_list'], body['answers_list'])
    }

    response = {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Credentials": "true",
        },
        "body": json.dumps(returnBody)
    }

    return response
