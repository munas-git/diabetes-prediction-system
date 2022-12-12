from flask import Flask, render_template, request

app = Flask(__name__)


# 



@app.route("/home/", methods=["POST", "GET"])
def home():
    if request.method == "GET":
        return(render_template("index.html"))

    elif request.method == "POST":

        # Collection of data from form.
        times_pregnant = request.form.get("NoPreg")
        glucose_concentration = request.form.get("GluCon")
        bp = request.form.get("BP")
        skin_fold = request.form.get("SFT")
        serum_insulin = request.form.get("SIL")
        bmi = request.form.get("BMI")
        bp = request.form.get("DP")
        age = request.form.get("Age")
        


if __name__ == "__main__":
    app.run()