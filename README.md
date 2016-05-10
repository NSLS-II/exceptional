# Exceptional

A client and server to post tracebacks to the NSLS2 DAMA slack chat

## Installation of client

```
conda install exceptional
```

Then in the ipython profile configuration, add these three lines

```python
import exceptional
exceptional.install_slack_notifier()
exceptional.HOST = 'penelope.cs.nsls2.local'
```

## Installation of server

```
git clone https://github.com/NSLS-II/exceptional
cd exceptional
python setup.py develop
```

You will need a slack API token.  For now let's assume you have one located
at ~/slack.token.

Start the flask server.

```
SLACK_TOKEN=`cat ~/slack.token` exceptional
```

Thats it!


## Notes

There will be a .json file located in ~/tb.json. This holds all of the
traceback information and it should probably be a little more robust than a
json file, assuming that we find this sort of thing useful.
