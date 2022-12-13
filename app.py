import pickle
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


# Deserialization of saved model.
model = pickle.load(open("final_model.pkl", "rb"))

session = {
    "result": ""
}


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
        # Storing result in session.
        session["result"] = result
        return redirect(url_for("result"))


@app.route("/result", methods= ["GET"])
def result():
    if session["result"] == 0:
        diagnosis = "Negative"
        message = "The doctor advices againsts heavy intake of heavily processed carbohydrates, sugar, red meat and processed meat. This would help reduce the risk of type 2 Diabetes"
        return(render_template("result.html", result_ = diagnosis, message_ = message))
    else:
        diagnosis = "Positive"
        message = "you are adised to schedule an appointment with a doctor close examination of your health situation. In order to avoid any further complications, you need to; Stop smoking if you currently smoke, keep your blood pressure and cholesterol under control, keep your vaccines up to date, pay attention to your feet, drink alcohol responsibly if you currently do so and take stress seriously."
        return(render_template("result.html", result_ = diagnosis, message_ = message))


if __name__ == "__main__":
    app.run()