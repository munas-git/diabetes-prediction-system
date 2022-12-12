import pickle
from flask import Flask, render_template, request

app = Flask(__name__)


# Deserialization of saved model.
model = pickle.load(open("final_model.pkl", "rb"))



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
        pedigree = request.form.get("DP")
        age = request.form.get("Age")

        # Storing variables in list.
        variables = [times_pregnant, glucose_concentration, bp, skin_fold, serum_insulin, bmi, pedigree, age]
        # Passing variables through model.
        result = model.predict([variables])

        if result[0] == 0:
            diagnosis = "Negative"
        else:
            diagnosis = "Positive"

        return(render_template("result.html", result_ = diagnosis))


if __name__ == "__main__":
    app.run()