from flask import Flask, redirect, url_for, render_template, request
from datetime import date
from AI_modified import prediction
import os
import fileman
app = Flask(__name__)
picture = os.path.join('static', 'images')
app.config['UPLOAD_FOLDER'] = picture
imageName = ''
@app.route("/", methods=["POST", "GET"])
def input():
    global imageName
    if request.method == "POST":
        fileman.filemgmt()
        user = request.form["ticker"]
        TickerSymbol = user
        # print("[DEBUG]TICKER SYMBOL =", user)
        option = request.form['radiobutton']
        print("[DEBUG] Include Date =", option)
        if option == 'yes':
            Date = True
            today = date.today()
            odtime = today.strftime("%Y-%m-%d")
            # print("[DEBUG] date =",odtime)
        else:
            Date = False
            odtime = None
            pass
        openvalue = request.form["openval"]
        custom_prediction = openvalue
        # print("[DEBUG] openval =", openvalue)
        predict = prediction(TickerSymbol, Date, custom_prediction, odtime)
        # print("[DEBUG] Prediction =", predict)
        imageName = TickerSymbol
        return redirect(url_for("user", value=predict))
    else:
        return render_template("input.html")

@app.route("/<value>")
def user(value):
    pic = os.path.join(picture, f"{imageName}.jpg")
    return render_template("Output_new.html", predict = value, image=pic) 

if __name__ == "__main__":
    app.run(debug=True)
