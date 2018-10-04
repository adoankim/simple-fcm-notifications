import os
import sys
from firebase_admin import initialize_app
from firebase_admin import credentials
from firebase_admin import messaging

def __show_cert_error_message__(details=None):
  print("\n" + "#" * 80, "\n")
  if details is not None:
    print("  " + details)
  print("\n  You can get it one for your project from:")
  print("\n\thttps://console.cloud.google.com/iam-admin/serviceaccounts")
  print("\n" + "#" * 80, "\n")

  sys.exit(-1)

if os.environ.get('CERTIFICATE_PATH') is None:
  __show_cert_error_message__(details="CERTIFICATE_PATH env var with the FCM credentials certificate must be set!")

try:
  cred = credentials.Certificate(os.environ.get('CERTIFICATE_PATH'))
  initialize_app(cred)
except:
  __show_cert_error_message__(details="The provided certificate file in CERTIFICATE_PATH is not valid")

invalid_request_data = ValueError("invalid_request_data")
error_sending_message = Exception("error_sending_message")
invalid_token = ValueError("invalid_token")

def send_message(token, request_data):
  try:
    message = __createMessage__(token, request_data)
    if message is not None:
      messaging.send(message)
      return True
    raise invalid_request_data
  except ValueError: 
    raise invalid_request_data
  except messaging.ApiCallError as err:
    __raise_fcm_error__(err)
  except:
    raise error_sending_message

def __raise_fcm_error__(err):
    if err.code is 'invalid-argument':
      raise invalid_token
    else:
      raise error_sending_message


def __createMessage__(token, request_data):
  notification = __create_notification__(request_data)
  if notification is None and request_data.get('data') is None:
    return None

  return messaging.Message(
      data=request_data.get('data'),
      token=token,
      notification=notification
  )

def __create_notification__(request_data):
  if request_data.get('notification') is None \
    or ('title' not in request_data['notification'] and 'body' not in request_data['notification']):
    return None
  
  notification_data = request_data['notification']
  return messaging.Notification(title=notification_data.get('title'), body=notification_data.get('body'))