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
from task import model_1
app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///db_Survey2.sqlite3'

db=SQLAlchemy(app)

class Survey(db.Model):
    __tablename__ = 'survey'
    id = db.Column(db.Integer, primary_key=True)
    time_spending = db.Column(db.Integer)
    reasons_using = db.Column(db.Integer)
    number_friends = db.Column(db.Integer)
    group_membership = db.Column(db.Integer)
    informational_use = db.Column(db.Integer)
    SIU_1 = db.Column(db.Integer)
    SIU_2 = db.Column(db.Integer)
    SIU_3 = db.Column(db.Integer)
    entertainment_use_1 = db.Column(db.Integer)
    entertainment_use_2 = db.Column(db.Integer)
    political_efficacy = db.Column(db.Integer)
    OEP_1 = db.Column(db.Integer)
    OEP_2 = db.Column(db.Integer)
    OEP_3 = db.Column(db.Integer)
    OEP_4 = db.Column(db.Integer)
    OFEP_1 = db.Column(db.Integer)
    OFEP_2 = db.Column(db.Integer)
    OFEP_3 = db.Column(db.Integer)
    OFEP_4 = db.Column(db.Integer)
    gender = db.Column(db.Integer)
    age = db.Column(db.String)
    birth_place = db.Column(db.Integer)
    education = db.Column(db.Integer)
    job = db.Column(db.Integer)
    income = db.Column(db.Integer)
    rural_ubran_1 = db.Column(db.Integer)
    location = db.Column(db.Integer)
    rural_urban2 = db.Column(db.Integer)
    fav_party = db.Column(db.Integer)
db.create_all()

#result_one, result_two,result_three, reg_metric_output=main_fun(y,X)
#linerity(df2)
#normality(y, regresion_results)
#homoscedasticity(y, regresion_results)
#corr=multicollinearity(df2)
@app.route('/')
def home():
    return render_template('main_survey.html')
@app.route('/survey', methods = ['GET', 'POST'])
def survey():
    a=0
    b=[]
    c=0
    d=[]
    e=0
    f=0
    g=0
    h=0
    i=0
    j=0
    k=0
    l=0
    m=0
    n=0
    o=[]
    p=0
    q=0
    r=0
    s=0
    t=0
    u=""
    v=0
    w=0
    aa=0
    bb=0
    cc=0
    dd=0
    ee=0
    ff=0
    if request.method=='POST':
        a=request.form.get('timespending')
        b=request.form.getlist('reson_using')
        b=','.join(b)
        c = request.form.get('friend')
        d = request.form.getlist('group_membersihp')
        d = ','.join(d)
        e=request.form.get('information_use')
        f=request.form.get('SIU_1')
        g=request.form.get('SIU_2')
        h = request.form.get('SIU_3')
        i=request.form.get('entertainment_use1')
        j=request.form.get('entertainment_use2')
        k = request.form.get('political_efficacy')
        l = request.form.get('OEP_1')
        m = request.form.get('OEP_2')
        n= request.form.get('OEP_3')
        o = request.form.get('OEP_4')
        p = request.form.get('OFEP_1')
        q = request.form.get('OFEP_2')
        r = request.form.get('OFEP_3')
        s = request.form.get('OFEP_4')
        t = request.form.get('gender')
        u = request.form.get('age')
        v = request.form.get('birthplace')
        w = request.form.get('education')
        aa = request.form.get('job')
        bb = request.form.get('income')
        cc = request.form.get('rural_urban1')
        dd= request.form.get('location')
        ee = request.form.get('ruaral_urban2')
        ff = request.form.get('party')
        answer=Survey(time_spending=a,reasons_using=b,number_friends = c,group_membership =d,informational_use =e, SIU_1=f,SIU_2=g,SIU_3=h,
                      entertainment_use_1=i,entertainment_use_2=j,political_efficacy=k,OEP_1=l, OEP_2=m,OEP_3=n,OEP_4=o, OFEP_1=p, OFEP_2=q,
                      OFEP_3=r, OFEP_4=s, gender=t,age=u,birth_place=v, education=w, job=aa,income=bb,rural_ubran_1=cc, location=dd,rural_urban2=ee,
                      fav_party=ff)
        db.session.add(answer)
        db.session.commit()
        return render_template("successful.html", result1=a,result2=b,result3=c,result4=d,result5=e)
    return render_template('survey.html')
if __name__ == '__main__':
    app.run(debug=True)


