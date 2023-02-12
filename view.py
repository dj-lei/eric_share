import warnings
from utils import *
from flask import Flask, jsonify, request, send_file, render_template, redirect
import sys

app = Flask(__name__)

@app.after_request
def apply_caching(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,*')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route("/query_configs", methods=['GET'])
def query_configs():
    if request.method == 'GET':
        configs = iterate_files_in_directory(cf['ENV_'+env]['TEXT_ANALYSIS_CONFIGS_STORE_PATH'])
        return jsonify({'status': 'ok', 'configs': configs})
    return jsonify({'status': 'error'})

@app.route("/save_config", methods=['GET'])
def save_config():
    if request.method == 'GET':
        filename = request.args.get('filename')
        config = request.args.get('config')
        path = cf['ENV_'+env]['TEXT_ANALYSIS_CONFIGS_STORE_PATH']+filename.split('\\')[-1]
        f = open(path, "w")
        f.write(config)
        f.close()
        return jsonify({'status': 'ok'})
    return jsonify({'status': 'error'})

@app.route("/download_config/<filename>", methods=['GET'])
def download_config(filename):
    if request.method == 'GET':
        filename = request.view_args['filename']
        return send_file(cf['ENV_'+env]['TEXT_ANALYSIS_CONFIGS_STORE_PATH']+filename)
    return jsonify({'status': 'error'})

@app.route("/")
def index():
    return render_template("index.html", files=iterate_files_in_directory(cf['ENV_'+env]['TEXT_ANALYSIS_APPS_STORE_PATH']))

# simple files server
@app.route("/download/<filename>")
def download(filename):
    path = cf['ENV_'+env]['TEXT_ANALYSIS_APPS_STORE_PATH']+filename
    return send_file(path)

# simple online video server
@app.route("/display/<filename>")
def display(filename):
    return redirect(cf['ENV_'+env]['TEXT_ANALYSIS_COURSE_PATH'] + filename, code=301)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001)