#!C:\Python310\python.exe
from flask import Flask, url_for, render_template
from waitress import serve 
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == '__main__':
    serve(app, host='local.jare.com', port=80)