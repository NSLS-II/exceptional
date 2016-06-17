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

### Build the docker containers
1. navigate to the exceptional git repo
```bash
docker build -t ericdill:exceptional (username:containername)
mkdir -p /tmp/data (/path/to/database/dir)
docker run -p 5000:5000 \
    -v /tmp/data:/data \
    -e DB_PATH="/data/db.json" \
    -e SLACK_TOKEN=`cat ~/dev/dotfiles/tokens/edill.slack` \
    -d \
    "ericdill/exceptional"
```

TODO: Configure docker hub to build new containers on push.

## Notes

There will be a .json file located in ~/tb.json. This holds all of the
traceback information and it should probably be a little more robust than a
json file, assuming that we find this sort of thing useful.
