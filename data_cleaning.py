#importing necessary library
import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from flask import Flask, render_template,flash, request
from wtforms import Form, StringField, validators, SubmitField, SelectField
from bioinfokit.analys import get_data, stat
#Importing SQLAlcheny
from flask_sqlalchemy import SQLAlchemy
#from custom_validators import height_validator, weight_validator
from myModules import results_summary_to_dataframe, result_one,results_two, main_fun, reg_metric, linerity,normality,homoscedasticity,multicollinearity


df = pd.read_csv("D:/Kyaw Thet/Thesis/MainProject/Dataset_2/old.csv")
print(df.head())

#To generate the online expressive political participation
df["OEP"]=((df["OEP_1"]/5)+(df["OEP_2"]/5)+(df["OEP_3"]/5)+(df["OEP_4"]/5))/4

#To generate the offline expressive political participation
df["OFEP"]=(df["OFEP_1"]+ df["OFEP_2"]+ df["OFEP_3"] +df["OFEP_4"])/4

#To generate the Social Interactional Usage
df["SIU"]=(df["SIU_1"]/5+(df["SIU_2"]/5)+(df["SIU_3"]/5)+(df["SIU_INGroup"]/4))/4

#To generate the three usage
df["three_usage"]=((df["informational_use"]/5)+ df["SIU"]+ (df["entertainment_use"]/5))/3

#print(df.dropna())
#print(df.isnull())

df.to_csv("D:/Kyaw Thet/Thesis/MainProject/Dataset/data_cleaning.csv")
print(df.head())
