import json
import uuid
import os
from flask import Flask, request, jsonify
from pprint import pprint
from tinydb import TinyDB, Query
from slacker import Slacker


db = TinyDB('/home/edill/tb.json')

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
error: {error}"""


def notify_slack(tb_info):
    error_msg = tb_info['formatted_exception'].split('\n')[-2]
    msg = slack_message_template.format(
        **{'beamline': tb_info['host_info'][1],
           'uid': tb_info['uid'],
           'error': error_msg}
    )
    slack.chat.post_message("#nsa", msg)


def insert(tb_info):
    db.insert(tb_info)

def start():
    app.run(host='0.0.0.0', port=5000, debug=True)
