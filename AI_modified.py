# Author : Akarshan Mishra
import yfinance as yf
import numpy as np
import pandas as pd
import sklearn
from sklearn import linear_model
import pickle
import matplotlib.pyplot as plt
from matplotlib import style
from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta
import mplcyberpunk

def prediction(TickerSymbol, Date=False, custom_prediction=0, odtime=None):
    endDay = datetime.today() - timedelta(days=1)
    endDay = endDay.date()
    delta = relativedelta(months=6)
    startDay = endDay - delta
    endDay = datetime.today()
    endDay = endDay.date()
    startDay -= timedelta(days=1)
    getFbinfo = yf.Ticker(TickerSymbol)
    history = getFbinfo.history(start=startDay, end=endDay)
    history.to_csv("{}.csv".format(TickerSymbol))
    data = pd.read_csv("{}.csv".format(TickerSymbol))
    ordinalTime = []
    for i in data["Date"]:
        i = datetime.strptime(i, "%Y-%m-%d") 
        ordinalTime.append(i.toordinal())
    df = pd.read_csv("{}.csv".format(TickerSymbol))
    df['OrdinalTime'] = ordinalTime
    df.to_csv("{}.csv".format(TickerSymbol))
    if Date == True:
        dataRead = pd.read_csv("{}.csv".format(TickerSymbol))
        history = dataRead[["Open", "Close", "OrdinalTime"]]
    elif Date == False:
        dataRead = pd.read_csv("{}.csv".format(TickerSymbol))
        history = dataRead[["Open", "Close"]]
    predict = "Close"
    X = np.array(history.drop([predict], 1))
    y = np.array(history[predict]) 
    bestModel = 0
    for _ in range(100):
        x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.1)
        linearRegression = linear_model.LinearRegression()
        linearRegression.fit(x_train, y_train)
        accuracy= linearRegression.score(x_test, y_test)
        if accuracy > bestModel:
            bestModel = accuracy
            with open("{}.pickle".format(TickerSymbol), "wb") as f:
                pickle.dump(linearRegression, f)
    # print(bestModel)
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.1)
    pickle_in = open("{}.pickle".format(TickerSymbol), "rb")
    regression = pickle.load(pickle_in)
    if Date == True:
        odtime = datetime.strptime(odtime, "%Y-%m-%d")
        predict2 = regression.predict([[custom_prediction, odtime.toordinal()]])
        out_arr = np.array_str(predict2)
        dataF = pd.DataFrame({'Actual Closing value':y_test, 'Predicted Closing value':regression.predict(x_test)})
        style.use("cyberpunk")
        dataF.plot(marker='o').set_title("{} Stocks - Prediction with date : {}".format(TickerSymbol, date.today()))
        plt.figtext(.84, .95, f'Accuracy = {round(bestModel*100)}%')
        plt.grid()
        mplcyberpunk.add_glow_effects()
        plt.savefig("static/images/{}.jpg".format(TickerSymbol), dpi=100)
        return out_arr.replace('[', '').replace(']', '')
    elif Date == False:
        predict2 = regression.predict([[custom_prediction]])
        out_arr = np.array_str(predict2)
        dataF = pd.DataFrame({'Closing value':y_test, 'Predicted Closing value':regression.predict(x_test)})
        style.use("cyberpunk")
        dataF.plot(marker='o').set_title("{} Stocks - Prediction without date".format(TickerSymbol))
        plt.figtext(.84, .95, f'Accuracy = {round(bestModel*100)}%')
        plt.grid()
        mplcyberpunk.add_glow_effects()
        plt.savefig("static/images/{}.jpg".format(TickerSymbol), dpi=100)
        return out_arr.replace('[', '').replace(']', '')
    
# predic = prediction(TickerSymbol="FB", Date=True, custom_prediction=333.02, odtime="2022-01-5")
# print(predic)