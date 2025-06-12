def handler(event, context):
    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'text/plain'},
        'body': 'Bonjour depuis bienvenu a ce lab sur le CDK!'
    }