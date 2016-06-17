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
exceptional.HOST = 'bcart01'
```

## Installation of server

There are a number of things that need to be specified in order for this
app to work

- docker image to run (nsls2/exceptional)
- data storage folder (/exceptional/data)
- database name (/exceptional/data/db.json)
- host (bcart01)
- port (5000)
- slack token

### Build the docker containers
New images are built on docker hub when new code is pushed to this git repo
and are available from nsls2/exceptional

## Notes

There will be a .json file located in ~/tb.json. This holds all of the
traceback information and it should probably be a little more robust than a
json file, assuming that we find this sort of thing useful.
