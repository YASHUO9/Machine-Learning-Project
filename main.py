# from data_cleaning import files_reading
# from combine import combining_csv
# from logistic_task import cleaning_and_prediction
from flask import Flask, render_template,request


from flask import Flask, render_template, session, redirect, url_for, session, flash
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField,
                     RadioField,SelectField,TextField,
                     TextAreaField,SubmitField)
from wtforms.validators import DataRequired

app.config['SECRET_KEY'] = 'mysecretkey'


app = Flask(__name__)

@app.route('/')
def index1():
    return render_template('home.html')

# @app.route('/report')
# def report():
        
#     first = request.args.get('UserName')
#     ress = False
#     for ele in first:# checking for uppercase character
#         if ele.isupper():
#             ress = True
#             break
#     res = any(chr.isdigit() for chr in first)    
#     lower_letter = any(c.islower() for c in first)
#     if res and ress and lower_letter:
#         return  render_template('passs.html')
#     else:
#         return  render_template('not_pass.html')
    
# if ress and res is True:
#     return render_template('index1.html')




if __name__=="__main__":
    app.run(debug=True)



























