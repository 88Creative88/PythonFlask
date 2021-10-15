from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
# from app import app
from flaskext.mysql import MySQL
import cursor as cursor
import pymysql
from flask import jsonify
from flask import flash, request
import requests
import auth
import mysql.connector
from requests.auth import HTTPBasicAuth
app = Flask(__name__)
CORS(app)



# Config

mydb = mysql.connector.connect(
host="fhdatenbank.database.windows.net",
user="niki",
password="Niklas8as",
database="fhdata"
)
#mydb = mysql.connector.connect(
 # host="127.0.0.1 ",
  #user="root",
  #password="Niklas8as",
  #database="fhdata"
#)



# routes


@app.route('/')
def get():
    return jsonify({'msg': 'Helloo World'})




@app.route('/addtobt1', methods=["GET", "POST"])
def add_tobt1():
     
    req =requests.get('fhdatenbank.database.windows.net', auth=HTTPBasicAuth('root', '1234'))
    if req:
    
        mycursor = mydb.cursor()
        sql = "INSERT INTO zeit_BT(Tag, zeit_senden) VALUES(CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)"
        val = ()
        mycursor.execute(sql, val)
        mydb.commit()
        respone = jsonify('geschrieben')
        respone.status_code = 200
        return respone
        
    else:
        respone = jsonify('falsch')
        respone.status_code = 402
        return respone
    
@app.route('/addtobt2', methods=["GET", "POST"])
def add_tobt2():
     
    req =requests.get('fhdatenbank.database.windows.net', auth=HTTPBasicAuth('root', '1234'))
    if req:
    
        mycursor = mydb.cursor()
        sql = "UPDATE zeit_BT SET zeit_licht=CURRENT_TIMESTAMP WHERE ID = (SELECT MAX(ID) FROM zeit_bt);"
        val = ()
        mycursor.execute(sql, val)
        mydb.commit()
        respone = jsonify('geschrieben')
        respone.status_code = 200
        return respone
        
    else:
        respone = jsonify('falsch')
        respone.status_code = 402
        return respone   

@app.route('/addtoth1', methods=["GET", "POST"])
def add_tobth1():
     
    req =requests.get('fhdatenbank.database.windows.net', auth=HTTPBasicAuth('root', '1234'))
    if req:
    
        mycursor = mydb.cursor()
        sql = "INSERT INTO zeit_TH(Tag, zeit_senden) VALUES(CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)"
        val = ()
        mycursor.execute(sql, val)
        mydb.commit()
        respone = jsonify('geschrieben')
        respone.status_code = 200
        return respone
        
    else:
        respone = jsonify('falsch')
        respone.status_code = 402
        return respone
    
@app.route('/addtoth2', methods=["GET", "POST"])
def add_toth2():
     
    req =requests.get('fhdatenbank.database.windows.net', auth=HTTPBasicAuth('root', '1234'))
    if req:
    
        mycursor = mydb.cursor()
        sql = "UPDATE zeit_TH SET zeit_licht=CURRENT_TIMESTAMP WHERE ID = (SELECT MAX(ID) FROM zeit_th);"
        val = ()
        mycursor.execute(sql, val)
        mydb.commit()
        respone = jsonify('geschrieben')
        respone.status_code = 200
        return respone
        
    else:
        respone = jsonify('falsch')
        respone.status_code = 402
        return respone   

@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Record not found: ' + request.url,
    }
    respone = jsonify(message)
    respone.status_code = 404
    return respone

if __name__ == "__main__":
    app.run()
