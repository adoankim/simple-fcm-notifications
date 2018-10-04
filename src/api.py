from flask import Flask
from flask import request
from fcm import send_message
from flask import json

app = Flask(__name__)

@app.route('/notification/<string:token>', methods=['POST'])
def notification(token):
    try:
        result = send_message(token, request.json)
    except Exception as err:
        result = err
    
    status, response = __build_response__(result)
    
    return app.response_class(
        response=response,
        status=status,
        mimetype='application/json'
    )

def __build_response__(result):
    status = None
    message = None
    if result is True:
        status = 200
        message = 'Notification sent correctly'
    elif result.__str__() is 'invalid_token':
        status = 400
        message = 'The provided token is not valid'
    elif result.__str__() is 'invalid_request_data':
        status = 400
        message = 'malformed notification payload'
    elif result.__str__() is 'error_sending_message':
        status = 500
        message = 'Couldn\'t send the message to the given token'    

    return (status, json.dumps({ "message": message }))