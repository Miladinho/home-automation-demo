from home import Home
from inMemoryRepository import InMemoryRepository
import json

from flask_cors import CORS
from flask import Flask, request, make_response
app = Flask(__name__)

repo = InMemoryRepository()
home = Home(repo)
home.initBaseComponents()

@app.after_request
def after_request(response):
  response.headers.add("Access-Control-Allow-Origin", "*")
  response.headers.add("Access-Control-Allow-Headers", "Content-Type, Access-Control-Allow-Headers")
  response.headers.add("Access-Control-Allow-Methods", "GET,POST,DELETE,PUT,OPTIONS")
  response.headers.add("Content-Type", "application/json")
  return response

@app.route("/")
def hello_world():
    return "Home Automation Demo API"

@app.route("/api/components", methods=["GET"])
def getAllComponents():
    lights = home.getLights()
    lights.append(home.getThermostat())
    return jsonResponse({"components": list(map(lambda item: item.__dict__, lights))})

@app.route("/api/components/thermostat", methods=["PUT"])
def updateThermostat():
    if request.method == "PUT":
        body = json.loads(request.data)
        home.setTemperature(int(body["value"]))
        return jsonResponse({"meesage": "Successfully updated thermostat"})
    return jsonResponse({"message": "Method "+request.method+" not supported."}, 405)

@app.route("/api/components/light/<string:name>", methods=["DELETE", "PUT", "POST"])
def updateLight(name):
    print(request)
    if request.method == "PUT":
        try:
            body = json.loads(request.data)
            home.setLightStatus(name, int(body["status"]))
            return jsonResponse({"message": "Successfully updated light " + name})
        except Exception as err:
            return jsonResponse({"message": str(err.args[0])}, 400)
    elif request.method == "DELETE":
        try:
            home.removeLight(name)
            return jsonResponse({"message": "Successfully updated light " + name})
        except Exception as err:
            return jsonResponse({"message": str(err.args[0])}, 400)
    elif request.method == "POST":
        try:
            print(name)
            body = json.loads(request.data)
            home.addLight(body["name"])
            return jsonResponse({"message": "Successfully added a new light light " + body["name"]})
        except Exception as err:
            print(err.args[0])
            return jsonResponse({"message": str(err.args[0])}, 404)
    return jsonResponse({"message": "Method "+request.method+" not supported."}, 405)

def jsonResponse(payload, status=200):
    payload["statusCode"] = status
    return (json.dumps(payload), status, {"Content-Type": "application/json"})





