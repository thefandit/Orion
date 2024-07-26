from flask import Flask, render_template
import logging, conf, logging.config

SERVER_PORT = 5000
SERVER_HOST = "0.0.0.0"

app = Flask(__name__)
logging.config.dictConfig(conf.dictConfig)
logger = logging.getLogger(__name__)

@app.route("/")
def index():

    logger.debug("requested /")

    return render_template("index.html")

@app.route("/increment/<key>/<amount>", method="POST")
def increment(key, amount):

    logger.debug("incrementing <" + key + "> by <" + amount + ">")

    return render_template("inventory.html")

@app.route("/decrement/<key>/<amount>", method="POST")
def decrement(key, amount):

    logger.debug("decrementing <" + key + "> by <" + amount + ">")

    return render_template("inventory.html")


if __name__ == "__main__":
    logger.debug("Starting Server at: " + SERVER_HOST + ":" + str(SERVER_PORT))
    app.run(SERVER_HOST, SERVER_PORT)
