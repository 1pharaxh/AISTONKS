# AISTONKS └(^o^ )┘
This is a python Flask app that predicts closing value for provided stock ticker symbol 
for the same date either using its past 6 months opening values or past 6 months opening values 
with their corresponding dates. The frontend was designed with CSS and javascript while python Flask controls the backend.

The machine learning algorithm is a simple linear regression model, the model is trained and tested 100 times and the model 
with best accuracy is pickled and loaded for prediction using user input. After each runtime the program also does
the cleanup of previously generated CSV file (used for trainining and testing), the model and .jpg graph of the model illustrating its accuracy

This app can be hosted on heroku with the included procfile.

Feel free to use my code for your projects but if you can then please credit me :)

DISCLAIMER: This project is only for "educational-purpose" PLEASE DO NOT use this project as any financial tool!

# Find this  project is hosted on:
http://aistonkss.herokuapp.com/

# Demonstration
![AISTONKS!](https://user-images.githubusercontent.com/93630550/148630690-3ccb68b0-91af-4225-9da9-6105fabd27a3.gif)
