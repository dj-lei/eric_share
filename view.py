import warnings
from utils import *
from flask import Flask, jsonify, request, send_file
app = Flask(__name__)


@app.after_request
def apply_caching(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,*')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route("/query_themes", methods=['GET'])
def query_themes():
    if request.method == 'GET':
        themes = iterate_files_in_directory(cf['ENV_'+env]['TEXT_LOGIC_CONFIG_STORE_PATH'])
        return jsonify({'status': 'ok', 'themes': themes})
    return jsonify({'status': 'error'})

@app.route("/save_theme", methods=['GET'])
def save_theme():
    if request.method == 'GET':
        filename = request.args.get('filename')
        theme = request.args.get('theme')
        path = cf['ENV_'+env]['TEXT_LOGIC_CONFIG_STORE_PATH']+filename.split('\\')[-1]
        f = open(path, "w")
        f.write(theme)
        f.close()
        return jsonify({'status': 'ok'})
    return jsonify({'status': 'error'})

@app.route("/download_theme/<filename>", methods=['GET'])
def download_theme(filename):
    if request.method == 'GET':
        filename = request.view_args['filename']
        return send_file(cf['ENV_'+env]['TEXT_LOGIC_CONFIG_STORE_PATH']+filename)
    return jsonify({'status': 'error'})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8001)