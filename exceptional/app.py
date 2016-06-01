import json
import uuid
import os
from flask import Flask, request, jsonify
from pprint import pprint
from tinydb import TinyDB, Query
from slacker import Slacker


db = TinyDB(os.path.join(os.path.expanduser('~'), 'tb.json'))
PORT = 5000
SLACK_TOKEN = os.environ.get('SLACK_TOKEN')
print("SLACK_TOKEN={}".format(SLACK_TOKEN))
slack = Slacker(SLACK_TOKEN)

DEBUG = True
app = Flask(__name__)

@app.route('/tb/<uid>')
def render_single_traceback(uid):
    return jsonify(db.search(Query().uid == uid)[0])

@app.route('/notify', methods=['POST'])
def notify():
    uid = str(uuid.uuid4())
    print("logging event {}".format(uid))
    tb_info = json.loads(request.get_json())
    tb_info['uid'] = uid
    insert(tb_info)
    notify_slack(tb_info)
    pprint(tb_info)
    return uid


slack_message_template = """New traceback from {beamline}
uid: {uid}
error: {error}
See the full traceback at: {url}
"""


def notify_slack(tb_info):
    error_msg = tb_info['formatted_exception'].split('\n')[-2]
    uid = tb_info['uid']
    url = 'https://{hostname}:{port}/tb/{uid}'.format(
        hostname=os.uname()[1],
        port=PORT,
        uid=uid,
    )
    msg = slack_message_template.format(
        beamline=tb_info['host_info'][1],
        uid=uid,
        error=error_msg,
        url=url
    )
    slack.chat.post_message("#nsa", msg)


def insert(tb_info):
    db.insert(tb_info)

def start(port=None):
    if port is None:
        port = PORT
    app.run(host='0.0.0.0', port=port, debug=True)
