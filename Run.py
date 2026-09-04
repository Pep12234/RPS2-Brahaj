from flask import Flask

app = Flask(__name__)

APP_ADDRES = "0.0.0.0"
APP_PORT = 5000

app.config["DEBUG"] = True
app.run(host = APP_ADDRES, port = APP_PORT)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"