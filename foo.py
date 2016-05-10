# import exceptional
# exceptional.install_slack_notifier()

import requests
requests.post('http://localhost:5000/notify', json={"foo": "bar"})
