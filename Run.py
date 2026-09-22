# SYSTEM LIBRARIES
from flask import Flask

# MY libraries
from module import dbConfig
from module import dbLogic

app = Flask(__name__)

APP_ADDRES = "0.0.0.0"
APP_PORT = 5000

@app.route("/", methods = ["GET", "POST"])
def index():
    data = {
        "uspeh" : False 
    }
    data["uspeh"] = dbLogic.getAll()
    return render_template("index.html")
    
app.config["DEBUG"] = True
app.run(host = APP_ADDRES, port = APP_PORT)

