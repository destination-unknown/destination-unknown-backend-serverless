import json
import main_exp

def hello(event, context):
    body = json.loads(event['body'])

    returnBody = {
        "countries": main_exp.determineChoice(body['questions_list'], body['answers_list'])
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
