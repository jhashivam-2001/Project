# Project
Hackathon project-----Predicting optimum purchase amount for raw materials in a restaurant.
Welcome to my project !
Training dataset source - https://www.kaggle.com/nilaydesmukh/restaurant-food-consumption
*****************************************************************************************************************************************************************
This project is basically an idea to create a classifier model that will help a restaurant owner estimate the quantity of each menu item that can be in demand on a certain day predicted against several variables like no. of people on the table,day of the week and time of the day.
This prediction would help the owner to estimate the optimum amount of raw materials that need to be purchased so that perishable raw materials won,t be wasted due to excess purchase.
This idea can be further evolved to work on a larger scale by taking the client as food factory units where perishable goods are wasted more due to logistic or climate issues.
This model not only will reduce food wastage but will also serve as a means to help restaurant owners optimize their budget.

*****************************************************************************************************************************************************************
TECH-STACK:-
 For the client end of the api created in flask, the inputs in Day field will be in the format "1 for Monday...2 for tuesaday and so on till 7 for sunday".
 We first did some exploratory data analysis on the data and plotted graphs to visualize the dependency of variables on each other.
 Using Linear Regression model would have been absurd because the target data is not continuous and moreover 3.6 plates of chicken curry is a meaningless output :-p
 Now in classification method i first went for K NearestNeighbours but the problem there was, since the data was overlapping much i was unable to achieve a perfect bias-variance tradeoff even after trying several values of K.
 Lastly I selected Random Forest Classifier over Decision Trees because when data has several categorical columns like mine bagged decision trees teend to be more corelated and the variance is much, which cant be lowered by averaging.
 ..In random forest algo since a fresh set of m random variable features out of total p features is selected at each split the trees are independent enough that the variance can be easily minimized by averaging.
 Jupyter notebook shows a classification report with average 95% accuracy and a f1 score of 97% in particular !
 
