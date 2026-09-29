# SYSTEM LIBRARIES
from flask import Flask
from flask import request

# MY libraries
from module import dbConfig
from module import dbLogic

app = Flask(__name__)

APP_ADDRES = "0.0.0.0"
APP_PORT = 5000

@app.route("/", methods = ["GET", "POST"])
def index():
    data = {
        "uspeh" : False,
        "itm" : None,
        "teza": "",
        "visina": ""
    }
    data["uspeh"] = dbLogic.getAll()
    if request.method == "POST"
        data["teza"] = request.form.get("teza")
        data["visina"] = request.form.get("visina")
        data["itm"] = izracunaj_itm(data[visina])
        
        if data["teza"] and data["visina"]:
            data["itm"] = izracunaj_itm(float(data[visina]), float(data["teza"])) 
        
        print(data)
    
    return render_template("index.html", podatki = data)
    
def izracunaj_itm(visinaCm, tezaKg):
    itm = tezaKg / (visinaCm/100) **2
    return itm 


app.config["DEBUG"] = True
app.run(host = APP_ADDRES, port = APP_PORT)

nobo