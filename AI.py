import yfinance as yf
import numpy as np
import pandas as pd
import sklearn
from sklearn import linear_model
from datetime import datetime
import pickle
'''
This function takes in TickerSymbol and makes
a CSV file (pre-processing) for it with the past 
1 year history of the stocks with Ordinal Time 
added as a column.
'''
def CSVsetup(TickerSymbol):
    # Setting Ticker Symbol.
    getFbinfo = yf.Ticker(TickerSymbol)

    # Getting past 6 month history of the Ticker.
    history = getFbinfo.history(period="6mo")

    # Saving the history to a CSV of the TickerSymbol name.
    history.to_csv("{}.csv".format(TickerSymbol))
    
    # Reading the stored CSV into data variable.
    data = pd.read_csv("{}.csv".format(TickerSymbol))

    # Generating integer value for time here and appending it 
    # to the previously generated CSV file.
    ordinalTime = []
    for i in data["Date"]:

        # Converting strings inside data["Date"] into
        # datetime objects
        i = datetime.strptime(i, "%Y-%m-%d")

        # Appending ordinal time to the list.
        ordinalTime.append(i.toordinal())
    df = pd.read_csv("{}.csv".format(TickerSymbol))

    # Making a new column called 'OrdinalTime' with  
    # same values of ordinalTime in the CSV file.
    df['OrdinalTime'] = ordinalTime
    df.to_csv("{}.csv".format(TickerSymbol))

# Setting flag for Date, if it is True then
# we look at the date for prediction.
Date = False

'''
This function takes an input of 1 or 
nothing, when it receives 1 then Date 
Flag is set to true.
'''
def inputFunc():
    global Date
    try:
        if input() == '1':
            Date = True
    except Exception:
        pass

# Setting input for user.
TickerSymbol = input()

# Invoking the pre-processing function here.
CSVsetup(TickerSymbol)

# Invoking input function.
inputFunc()

# Setting conditions based on the 'Date' flag.
# if its True then we look at the 'OrdinalTime'
# column. Else we just look at the Opening Value.
if Date == True:
    dataRead = pd.read_csv("{}.csv".format(TickerSymbol))
    # Filtering useful attributes.
    history = dataRead[["Open", "Close", "OrdinalTime"]]
elif Date == False:
    dataRead = pd.read_csv("{}.csv".format(TickerSymbol))
    # Filtering useful attributes.
    history = dataRead[["Open", "Close"]]

# Predicting the lable "Close"
predict = "Close"

# Attribute array.
X = np.array(history.drop([predict], 1))

# Label array.
y = np.array(history[predict]) 

# Training Model n times for best accuracy
def prediction(X, y):
    bestModel = 0
    for _ in range(100):
        # x_test is testing Open value. y_test is testing closing value. Splitting 10% of our data into test samples for checking accuracy
        x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.1)

        linearRegression = linear_model.LinearRegression()
        # Fitting data to find best fit line.
        linearRegression.fit(x_train, y_train)

        # Finding accuracy of the prediction by comparing it to any 10% of data from the dataset.
        accuracy= linearRegression.score(x_test, y_test)

        # [Uncomment!] for debugging!
        # print("Accuracy: " + str(accuracy))
        
        # Saving the current model which has higher accuracy than the one we trained for.
        if accuracy > bestModel:
            bestModel = accuracy
            with open("{}.pickle".format(TickerSymbol), "wb") as f:
                pickle.dump(linearRegression, f)
    # [Uncomment!] for debugging!
    # return("Best Accuracy:", bestModel)

# Invoking the prediction function
prediction(X, y)
# x_test is testing Open value. y_test is testing closing value. Splitting 30% of our data into test samples for checking accuracy
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.1)

# Loading saved model here.
pickle_in = open("{}.pickle".format(TickerSymbol), "rb")
linearRegression = pickle.load(pickle_in)

def UserInput(Date):
    if Date == True:
        custom_prediction = float(input())
        odtime = input("Enter a Date in the format of YEAR-MONTH-DATE")
        odtime = datetime.strptime(odtime, "%Y-%m-%d")
        predict2 = linearRegression.predict([[custom_prediction, odtime.toordinal()]])
        out_arr = np.array_str(predict2)
        print('PREDICTION :', out_arr.replace('[', '').replace(']', ''))
    elif Date == False:
        custom_prediction = float(input())
        predict2 = linearRegression.predict([[custom_prediction]])
        out_arr = np.array_str(predict2)
        print('PREDICTION :', out_arr.replace('[', '').replace(']', ''))
UserInput(Date)
'''
The code below can be used to find the Coefficients of the 
regression equation with the intercepts. We can furthermore
check the predicted closing value, open value or Date, and 
Original Closing Value. 
'''
# print('Coefficient of equation :', linearRegression.coef_)
# print('Intercepts of equation :', linearRegression.intercept_)

# # This prints predicted closing value, Open value / Date, Original closing value.
# predictions = linearRegression.predict(x_test)
# for x in range(len(predictions)):
#     print('PREDICTED :',predictions[x], 'OPEN VALUE OR DATE:', x_test[x], 'ORIGNAL', y_test[x])