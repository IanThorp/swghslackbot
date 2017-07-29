import os
import time
import json
import requests
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello world!"

@app.route("/slack")
def touch_slack():
  params = {
    'token': token
    ,'ts_to': ts_to
    ,'count': 1000
  }
  uri = 'https://slack.com/api/files.list'
  response = requests.get(uri, params=params)
  return json.loads(response.text)['files']

@app.route("/")
if __name__ == "__main__":
  port = int(os.environ.get("PORT", 5000))
  app.run(host='0.0.0.0', port=port)
