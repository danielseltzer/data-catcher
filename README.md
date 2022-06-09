# Data Catcher Mini Service for IoT Data Collection

Runs in a docker container
Listens for restful requests to store some json

## ENV vars
Note you will need to create a `.env` file (you can use the `sample.env` and give it meaningful paths) like:
```
DATACATCHER_DATA_DIR=./data
HOST_DATA_DIR=/Volumes/datacatcher/data
```
