from flask import Flask
import server
from deta import Deta

app = Flask(__name__)
app.secret_key="test"

app.register_blueprint(server.bp)

@app.route("/hello/<name>",methods=["GET"])
def hello_world(name):
    return f"HELLO {name}"
