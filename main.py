from data_cleaning import files_reading
from combine import combining_csv
from logistic_task import cleaning_and_prediction



from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField)




app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

class InfoForm(FlaskForm):
    breed = StringField("What Breed are you?")
    submit = SubmitField("Submit")

@app.route('/')
def index1():
    return render_template('home.html')

@app.route('/report',methods=['GET','POST'])
def report():
        return render_template('index2.html')

@app.route("/start")
def start():
    files_reading()
    combining_csv()
    cleaning_and_prediction()
    
    return render_template('thank_you.html')
    



if __name__=="__main__":
    app.run(debug=True)



























