import numpy as np
import pickle
import json

class detail():
    def __init__(self,age,education,default,balance,housing,loan,duration,campaign,pdays,previous,marital,job,poutcome):
        self.age=age
        self.education=education
        self.default=default
        self.balance=balance
        self.housing=housing
        self.loan=loan
        self.duration=duration
        self.campaign=campaign
        self.pdays=pdays
        self.previous=previous
        self.marital=marital
        self.job=job
        self.poutcome=poutcome

    def bank_model(self):
        with open("bank_project.pickle","rb") as f:
            self.m=pickle.load(f)

        with open("columns_list.json","r") as f:
            self.jsn=json.load(f)

    def bank_pred(self):
        self.bank_model()

        arr=np.zeros(len(self.jsn["columns"]))

        arr[0]=self.age
        arr[1]=self.education
        arr[2]=self.default
        arr[3]=self.balance
        arr[4]=self.housing
        arr[5]=self.loan
        arr[6]=self.duration
        arr[7]=self.campaign
        arr[8]=self.pdays
        arr[9]=self.previous

        mar="marital_" + self.marital
        mar_index=self.jsn["columns"].index(mar)
        arr[mar_index]=1

        mar1="job_" + self.job
        mar_index1=self.jsn["columns"].index(mar1)
        arr[mar_index1]=1

        mar2="poutcome_" + self.poutcome
        mar_index2=self.jsn["columns"].index(mar2)
        arr[mar_index2]=1

        result=self.m.predict([arr])
        return result

