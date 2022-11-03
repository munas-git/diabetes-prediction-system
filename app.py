from crypt import methods
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/home/", methods=["POST", "GET"])
def home():
    return(render_template())

if __name__ == "__main__":
    app.run()