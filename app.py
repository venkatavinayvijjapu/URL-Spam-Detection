import numpy as np
from flask import Flask, request, jsonify, render_template,redirect
import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
#data_cleaned = pd.read_csv('models/data_final.csv')
app = Flask(__name__)
classifier = pickle.load(open("classifier.pkl", "rb"))
df=pd.read_csv('datathon_train.csv')
df.columns=['url','label']
df=df.dropna(axis=0,how='all')
df.isnull()
df['url'] = df['url'].map(lambda x:x.replace('//', ' '))
df['url'] = df['url'].map(lambda x:x.replace('/', ' '))
df['url'] = df['url'].map(lambda x:x.replace('-', ' '))
df['url'] = df['url'].map(lambda x:x.replace('.', ' '))
df['url'] = df['url'].map(lambda x:x.replace(',',' '))
x=df['url']
y=df['label']
tfidf=TfidfVectorizer(ngram_range=(1,3),lowercase=True)
x_train=tfidf.fit_transform(x)
@app.route('/',methods=['POST','GET']) 
def home():
    if request.method=="POST":
        print(request.form.to_dict())
        input_dict=request.form.to_dict()
        g=input_dict
        print(type(g))
        g=str(g)
        g=g.replace('//',' ')
        g=g.replace('/',' ')
        g=g.replace('-',' ')
        g=g.replace('.',' ')
        g=g.replace(',',' ')
        # tfidf=TfidfVectorizer(ngram_range=(1,3),lowercase=True)
        x=tfidf.transform([g])
        y_pred=classifier.predict(x) 
        if(y_pred==0):
            stri="Legit"
        else:
            stri="Not Legit"

    return render_template('index.html',pred=stri)
if __name__ == "__main__":
    app.run(debug=True)
