from flask import Flask, redirect, url_for, render_template, request
from datetime import date, datetime
from AI_modified import prediction
app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def input():
    if request.method == "POST":
        user = request.form["ticker"]
        TickerSymbol = user
        print("[DEBUG]TICKER SYMBOL =", user)
        option = request.form['options']
        print("[DEBUG] Include Date =", option)
        if option == 'yes':
            Date=True
            today = date.today()
            odtime = today.strftime("%Y-%m-%d")
            
            print("[DEBUG] date =",odtime)
        else:
            Date=False
            odtime = None
            pass
        openvalue = request.form["openval"]
        custom_prediction = openvalue
        print("[DEBUG] openval =", openvalue)
        predict = prediction(TickerSymbol, Date, custom_prediction, odtime)
        print("[DEBUG] Prediction =", predict)
        return redirect(url_for("user", value=predict))
    else:
        return render_template("input.html")


@app.route("/<value>")
def user(value):
    return f"<h1>Prediction = {value}</h1>"

if __name__ == "__main__":
    app.run(debug=True)