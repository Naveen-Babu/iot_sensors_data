from flask import Flask, jsonify, request, session, abort, flash, redirect
from flask import render_template
import time as t

app = Flask(__name__)
import os
import json
import datetime

d = 0


@app.route("/getdata/humidity/<h>/temperature/<temp>/distance/<d>/sensorValue/<sv>", methods=['GET']) #input route
def chart(h, temp, d, sv):
    print ("Inside here")
    # t.sleep(1)
    #hb_th = hb.split('$')[1]
    #tm_th = temp.split('$')[1]
    #sm_th = gas.split('$')[1]
    #hm_th = hum.split('$')[1]

    with open('sensor.json', 'r') as json_file1: #read format
        params1 = json.load(json_file1)
        json_file1.close()
        
        params1["Humidity"] = h.split('$')[0]
        params1['Temperature'] = temp.split('$')[0]
        params1['Distance'] = d.split('$')[0]
        params1['SensorValue'] = sv.split('$')[0]

       # params1["HB_Th"] = hb.split('$')[1]
       #params1['TEMP_Th'] = temp.split('$')[1]
       # params1['HUM_Th'] = hum.split('$')[1]
       #params1['SMO_Th'] = gas.split('$')[1]

    try:
        with open('sensor.json', 'w') as json_file1:
            json.dump(params1, json_file1)
    except Exception as e2:
        print(str(e2))

    return jsonify(params1)   #returns to client


@app.route("/dummy", methods=['GET'])
def dummies():
    print ("Inside dummies")

    with open('sensor.json') as json_file:  #read
        d = json.load(json_file)
        print("1234")
        print (d["Temperature"])

    return jsonify(temp=d["Temperature"], h=d["Humidity"], d=d["Distance"], sv=d["SensorValue"])


@app.route("/")     # o/p route
def hello():
    return render_template('home.html')


@app.route("/success" ,methods=['POST'])
def success():
    return "success"


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5010))

    print("Starting app on port %d" % port)

    app.run(debug=False, port=port, host='0.0.0.0')
