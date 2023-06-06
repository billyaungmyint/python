from flask import Flask
from flask import request, render_template
import joblib

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        rates = float(request.form.get("rates"))
        print(rates)
        model1 = joblib.load("regression.joblib")
        r1 = model1.predict([[rates]])
        model2 = joblib.load("tree.joblib")
        r2 = model2.predict([[rates]])
        return render_template("index.html", result1=r1, result2=r2)
    else:
        return render_template("index.html", result1="waiting", result2="waiting")


if __name__ == "__main__":
    app.run(debug=True)
