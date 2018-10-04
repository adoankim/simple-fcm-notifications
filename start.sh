#!/bin/bash
source ./virtual-environment/bin/activate

FLASK_PORT=8080

# we check that the given argument is a valid number
re='^[0-9]{4}$'
if ! [[ -z "$1" ]] && ! [[ $1 =~ $re ]]; then
  echo "Port argument must be a 4 digits number"
  echo "i.e: ./start.sh 8080"
  exit -1
fi

if ! [[ -z "$1" ]]; then
  FLASK_PORT=$1
fi


FLASK_APP=./src/api.py flask run --port=$FLASK_PORT