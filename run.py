from flask import Flask,render_template,request
import pickle
import numpy as np
import pandas as pd

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
   if request.method =='POST':
       
        Shift= request.form.get('Shift')
        Day= request.form.get('Day')
        PartySize= request.form.get('PartySize')
        MenuCateogry= request.form.get('MenuCateogry')
        MenuItem= request.form.get('MenuItem')
        ItemPrice= request.form.get('ItemPrice')
        data=[[Shift,Day,PartySize,MenuCateogry,MenuItem,ItemPrice]]
        df2=pd.DataFrame(data,columns=['Shift','Day','PartySize','MenuCateogry','MenuItem','ItemPrice'])
        df3=pd.get_dummies(df2,columns=["MenuCateogry","MenuItem","Shift"],drop_first=True)
        model=pickle.load(open('model.pkl','rb'))
        prediction=model.predict(df2) 
        return render_template('index.html',prediction=prediction)
    else:
        return "ERROR"
    


if __name__=='__main__':
    app.run(debug=True)