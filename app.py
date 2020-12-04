from flask import Flask, render_template, request, redirect, jsonify

from qr_convertor import qrify

app = Flask(__name__, static_folder='./static')

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.secret_key = 'my-secret-key'
app.config['SESSION_TYPE'] = 'filesystem'

@app.route("/", methods=['GET'])
def index():

    if request.method == 'GET':
        return render_template("index.html")

@app.route("/generate-qr", methods=['POST'])
def generate_qr():

    if request.method == 'POST':
        sentence = request.form['sentence']

        filename = qrify(sentence)

        return jsonify({"status": "Successfully generated QR!", "filename": filename})