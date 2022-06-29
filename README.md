# Data Catcher Mini Service for IoT Data Collection

Listens for restful requests to store some json.

Runs in a docker container, or you can run it as a direct python command.

## ENV vars
Note you will need to create a `.env` file (you can use the `sample.env` and give it meaningful paths) like:
```
DATACATCHER_DATA_DIR=./data
HOST_DATA_DIR=/Volumes/datacatcher/data
```
The `DATACATCHER_DATA_DIR` is where the service writes incoming data requests on disk. If you're running locally, as source, this is your local path.

The `HOST_DATA_DIR` is used in the docker configuration to specify where the container will look for the data directory to mount it properly. If you're running in a container, this is where the docker host process can find the data files.

