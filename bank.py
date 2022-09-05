from function import detail
from flask import Flask,redirect,url_for,render_template,request
bank=Flask(__name__)

@bank.route("/")
def welcome():
    return render_template("index.html")

@bank.route("/sac",methods=["POST"])
def sac():
    data=request.form

    age=int(data["age"])
    education=int(data["education"])
    default=int(data["default"])
    balance=int(data["balance"])
    housing=int(data['housing'])
    loan=int(data['loan'])
    duration=int(data['duration'])
    campaign=int(data['campaign'])
    pdays=int(data['pdays'])
    previous=int(data['previous'])
    marital=data['marital']
    job=data['job']
    poutcome=data['poutcome']

    final_result=detail(age,education,default,balance,housing,loan,duration,campaign,pdays,previous,marital,job,poutcome).bank_pred()

    return render_template("index.html",final=final_result)

if __name__=="__main__":
    bank.run(host="0.0.0.0",port=8080,debug=True)



