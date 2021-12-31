
import yfinance as yf
import numpy as np
import pandas as pd
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle

import pickle
import matplotlib.pyplot as plt
from matplotlib import style
# import datetime
# startDate = datetime.datetime(2021, 6, 30)
# endDate = datetime.datetime(2021,12,31)
TickerSymbol = "FB"
#Setting Ticker Symbol.
getFbinfo = yf.Ticker(TickerSymbol)

#Getting past 6 month history of the Ticker.
history = getFbinfo.history(period="6mo")
# Filtering useful attributes.
history = history[["Open", "High", "Low", "Close"]]

# Predicting the lable "Close"
predict = "Close"

# Attribute array.
X = np.array(history.drop([predict], 1))

# Label array.
y = np.array(history[predict]) 

# Splitting 30% of our data into test samples and train samples
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.3)
# # Training Model n times for best accuracy
# bestModel = 0
# for _ in range(15):
#     # Accuracy test. Splitting 30% of our data into test samples and train samples
#     x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.3)

#     linear = linear_model.LinearRegression()
#     # Fitting data to find best fit line.
#     linear.fit(x_train, y_train)
#     acc = linear.score(x_test, y_test)
#     print("Accuracy: " + str(acc))
    
#     # Saving the current model which has higher accuracy than the one we trained for.
#     if acc > bestModel:
#         bestModel = acc
#         with open("{}.pickle".format(TickerSymbol), "wb") as f:
#             pickle.dump(linear, f)
# print("Best Accuracy:", bestModel)

# Loading saved model here.
pickle_in = open("{}.pickle".format(TickerSymbol), "rb")
linear = pickle.load(pickle_in) 

print('Coefficient: \n', linear.coef_)
print('Intercept: \n', linear.intercept_)

predictions = linear.predict(x_test)

for x in range(len(predictions)):
    print(predictions[x], x_test[x], y_test[x])


