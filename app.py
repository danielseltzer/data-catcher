import bottle
from bottle import request, response
import json
from pathlib import Path
from time import time
import logging
import os


logging.basicConfig(level=logging.DEBUG)

app = bottle.default_app()

root_dir_key = 'DATA_CATCHER_ROOT_DIR'

@app.route('/')
def info():
    return 'This is the data catcher service.'


@app.post('/catch/<datatype>')
def data_catch(datatype='Any'):
    dest_dir = Path(base_dir) / datatype
    if not dest_dir.exists():
        logging.info(f'Making datatype dir: {dest_dir}')
        dest_dir.mkdir()

    json_file = dest_dir / f'catch-{int(time())}.json'

    with open(json_file, 'w+t') as outfile:
        json.dump(request.json, outfile)

    # return 200 Success
    response.headers['Content-Type'] = 'application/json'
    return json.dumps({'response': "OK"})


if __name__ == '__main__':
    logging.info('Starting up datacatcher...')
    base_path = os.getenv(root_dir_key)
    if base_path is None:
        base_path = Path.cwd()
        logging.warn(f'No ENV VAR found at {root_dir_key}, using {base_path}')

    base_dir = Path(base_path) / 'data'

    if not base_dir.exists():
        logging.info(f'Making data base dir: {base_dir}')
        base_dir.mkdir()

    logging.info(f'Base data dir is set to {base_dir}')

    logging.info(f'Listening on ')
    bottle.debug(True)
    bottle.run(app, host = '0.0.0.0', port=8000)

# host='localhost',
#
