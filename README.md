# Simple-FCM-API

This project exposes the Firebase Cloud Messaging (FCM) notification send through a REST API using the Firebase Admin SDK

## Requirements
  - Python >=3.x
  - Have a Firebase project with the FCM API enabled (https://console.cloud.google.com/apis/api/fcm.googleapis.com)
  - Access to a Google Cloud service account credentials that have permissions to use the FCM API 
    (https://console.cloud.google.com/iam-admin/serviceaccounts)

## Setup
```
git clone https://github.com/adoankim/simple-fcm-notifications.git
cd single-fcm-notifications
./setup.sh
```

## Running the server
```
CERTIFICATE_PATH=./path/to/your/service/account/certificate
start.sh [PORT_NUMBER]
```

The default port is: `8080`

## Sample request
```
curl -d '{"notification": { "title": "Simple-FCM", "body": "Hello world!" }}' \
     -H "Content-Type: application/json" \
     http://localhost:8080/notification/<DEVICE_FCM_TOKEN> -v
```

## Endpoints

> **Note**: All endpoints require the `application/json` header in the request.

---

#### POST /notification/<FCM_TOKEN>

- **Payload types:**

  - Only notification:
    ```
    { 
      "notification" : {
        "title": "this is a title",
        "body" : "this is a body"
      } 
    }
    ```

  - Only data:
    ```
    { 
      "data" : {
        "x": 20.0,
        "y": 35.5,
        "z": 40.5,
      } 
    }
    ```

  - Both:
    ```
    { 
      "notification" : {
        "title": "this is a title",
        "body" : "this is a body"
      },
      "data" : {
        "x": 20.0,
        "y": 35.5,
        "z": 40.5,
      }
    }
    ```

---

## TODOs
 - [ ] Serve an HTML form to send request from the browser   
 - [ ] Extend the API with other FCM functionalities 