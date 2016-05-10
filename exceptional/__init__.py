from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

import sys
import os
import IPython
import traceback as tb_module
import json
import requests


URL = 'localhost'
PORT = 5000


def notify_slack(**kwargs):
    """
    Send a notification to the DAMA slack channel
    """
    formatted_exception = tb_module.format_exc()
    host_info = os.uname()
    info = {
        'formatted_exception': formatted_exception,
        'host_info': host_info,
        'conda_env': os.environ.get('CONDA_ENV_PATH')
    }
    info.update(**kwargs)
    url = 'http://{url}:{port}/notify'.format(URL, PORT)
    r = requests.post(url, json=json.dumps(info))
    print("If you would like help with this exception, please post an issue at "
          "https://github.com/NSLS-II/Bug-Reports and reference this uid:\n\n "
          "\t\t{}".format(r.text))

def python_slack_notification_hook(exctype, value, traceback):
    """
    Custom exception hook that first sends the traceback to our slack channel
    and then continues to handle the exception normally.

    Thanks http://stackoverflow.com/a/6598286/3781327
    """
    notify_slack()
    # now let python actually handle the exception
    sys.__excepthook__(exctype, value, traceback)


def ipython_slack_notification_hook(self, etype, value, tb, tb_offset=None):
    """
    Custom exception hook that first sends info to our slack channel by way of
    a flask app and then shows the IPython traceback.

    Thanks https://mail.scipy.org/pipermail/ipython-dev/2012-April/008945.html
    The API has slightly changed from that email, so check out the official
    docs instead at http://ipython.org/ipython-doc/dev/api/generated/IPython.core.interactiveshell.html#IPython.core.interactiveshell.InteractiveShell.set_custom_exc
    """
    # h[0] is the session number
    # h[1] is the line number
    # h[2] is the command]
    ipython_history = [
        h[2] for h in IPython.get_ipython().history_manager.get_range()]
    notify_slack(ipython_history=ipython_history)
    IPython.get_ipython().showtraceback()


def install_slack_notifier():
    # install the python one
    sys.excepthook = python_slack_notification_hook
    # install the ipython one
    IPython.get_ipython().set_custom_exc(
        (Exception,), ipython_slack_notification_hook)

