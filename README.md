# Exceptional

A client and server to post tracebacks to the NSLS2 DAMA slack chat

## Conda Recipes

[tag](https://github.com/NSLS-II/lightsource2-recipes/tree/master/recipes-tag/event-model)

[dev](https://github.com/NSLS-II/lightsource2-recipes/tree/master/recipes-dev/event-model)

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

### Run the exceptioanl server

docker run -p 5000:5000 \
  -e DB_PATH="/exceptional/data/db.json" \
  -e SLACK_TOKEN=`cat /exceptional/slack.token` \
  -d \
  nsls2/exceptional

## Notes

The `DB_PATH` environmental variable that gets passed to the docker image will
be the location of the .json based database. This holds all of the
traceback information.
