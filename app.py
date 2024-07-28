from flask import Flask, render_template, jsonify, request
import logging, conf, logging.config
import jsonHandler
import json

SERVER_PORT = 5000
SERVER_HOST = "0.0.0.0"

app = Flask(__name__)
logging.config.dictConfig(conf.dictConfig)
logger = logging.getLogger(__name__)

@app.route("/")
def index():

    logger.debug("requested /")

    return render_template("index.html")

@app.route("/increment/<key>/<amount>", methods=['POST'])
def increment(key, amount):

    logger.debug("incrementing <" + key + "> by <" + amount + ">")

    return render_template("inventory.html")

@app.route("/decrement/<key>/<amount>", methods=['POST'])
def decrement(key, amount):

    logger.debug("decrementing <" + key + "> by <" + amount + ">")

    return render_template("inventory.html")

@app.route("/inventory")
def inventory():

    logger.debug("loading Inventory")

    return render_template("inventory.html")

    # return render_template("inventory.html")

@app.route("/getinventory", methods=['GET'])
def getInventory():

    logger.debug("Sending Inventory")

    dataToSend = jsonHandler.getJsonData()
    logger.debug(dataToSend)
    return jsonify(dataToSend)

if __name__ == "__main__":
    logger.debug("Starting Server at: " + SERVER_HOST + ":" + str(SERVER_PORT))
    app.run(SERVER_HOST, SERVER_PORT)
