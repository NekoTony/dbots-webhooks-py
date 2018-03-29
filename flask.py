from flask import Flask
import json
from datetime import datetime, date

app = Flask(__name__)

def cauth(auth, headers):
    if headers.get("authorization") is None:
        return None
    elif headers.get("authorization") == auth:
        return True
    return False

def get_userids(key=None):
    with open('/root/storage/upvotes.json', 'r') as x:
	    data = json.load(x)
    if key is None:
        return data
    elif data.get(key) is None:
        return False
    return data[key]

def get_config(key=None):
    with open('/root/storage/config.json', 'r') as x:
	    data = json.load(x)
    if key is None:
        return data
    return data[key]

def write_userids(key, id):
    data = get_userids()
    if get_userids(key) is False:
	if conf["miss"] == 1:
	    data = {}
        data[key] = []
        data[key + "_voted"] = []
    if id in data[key]:
        return "already_voted"
    data[key].append(id)
    with open('/root/storage/upvotes.json', 'w') as x:
        json.dump(data, x)
    return True

conf = get_config()

@app.route(conf["post"],methods=['POST'])
def dbotsorg():
    botid = conf["botid"]
    auth = conf["auth"]
    today = datetime.today().strftime('%Y-%m-%d')
    check = cauth(auth, request.headers)
    if request.method == 'POST' and check is not False:
        data = request.json
        if data["type"] == "upvote" and data["bot"] == botid:
            userid = data["user"]
            write_userids(today, userid)
    return ''

@app.route('/')
def hello_world():
    return 'Your server is up and running!'

if __name__ == '__main__':
   app.run(debug = True)
