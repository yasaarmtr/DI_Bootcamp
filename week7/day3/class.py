# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 10:33:51 2021

@author: Yasaar Mauthoor
"""
# import pandas as pd

# data = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")
# data = pd.get_dummies(data, columns = ["species"])
#-------------------------------------------------------
# url = 'https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv'
# cars_df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
# # data = pd.get_dummies(data, columns = [""])

# # print(cars_df['Origin'].isna().sum())
# # print(cars_df['Origin'].value_counts())
# cars_df.fillna('USA', inplace = True)
# # print(cars_df['Origin'].value_counts())
# cars_df = pd.get_dummies(cars_df, columns=['Origin'])
# print(cars_df)



# Target encoding example
# url = 'https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv'
# cars_df = pd.read_csv(url).dropna(subset=['Manufacturer', 'Price'])
# # Calculate meaningful information, the mean(like average) price for each manufacturer
# # means = cars_df[['Manufacturer', ‘Price’]].groupby('Manufacturer').mean()
# # # means = {“Acura” : 29.9} -> means[“Acura”] <> means.loc[“Acura”, “Price”]
# # # Add the above column to the original dataframe
# # cars_df['Manufacturer_transformed'] = cars_df['Manufacturer'].map(lambda x: means.loc[x, “Price”])
# # # Here we use .apply() - gives the same result as .map() and we replace
# # #Manufacturer with its mean price
# # cars_df['Manufacturer'] = cars_df[‘Manufacturer’].apply(lambda x: means.loc[x, “Price”])
# # #Reminder, how we add new keys and values to dictionaries
# # dict_1 = {‘One’: 1}
# # dict_1[‘Two’] = 2
# # #Replace NAN example
# # cars_df[‘DriveTrain’].isna().sum()
# # cars_df[‘DriveTrain’].value_counts()
# # cars_df.fillna(‘Front’, inplace = True)
# # cars_df[‘DriveTrain’].value_counts()

# print(cars_df['Type'].isna().sum())
# print(cars_df['Type'].value_counts())
# # cars_df.fillna('Small', inplace = True)
# cars_df = pd.read_csv(url).dropna(subset=['Type', 'Price'])
# print(cars_df['Type'].isna().sum())
# # cars_df["Manufacturer_transformed"] = cars_df["Manufacturer"].map(lambda x: means.loc[x, "Price"])

# median = cars_df[['Type','Price']].groupby("Type").median()
# print(median)
# cars_df['Type_transformed'] = cars_df['Type'].dropna().apply(lambda x:median.loc[x,'Price'])
# print(cars_df[["Type","Type_transformed","Price"]].head())



# # cars_df = pd.get_dummies(cars_df, columns=['Type'])
# # print(cars_df)


# cars_df.fit_transform(cars_df._get_numeric_data())


#------------------------------------------------------------------------------
import pandas as pd
import numpy as np 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from sklearn import preprocessing

dataframe = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

y = np.array(dataframe['species'])
X = dataframe.drop(['species'],axis=1)

s_scaler = StandardScaler()
X = s_scaler.fit_transform(X)

# y = pd.get_dummies(y, columns = ['species']) #for X preparation
le = preprocessing.LabelEncoder()
y = le.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)


from sklearn.linear_model import LogisticRegression
"""model"""
clf = LogisticRegression(random_state=0).fit(X_train, y_train)
r = clf.predict(X_test)

clf.score(X_test, y_test)





