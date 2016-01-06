from flask import Flask, render_template, flash
from flask_bootstrap import Bootstrap
from flask_appconfig import AppConfig
from flask_wtf import Form, RecaptchaField
from wtforms import TextField, HiddenField, ValidationError, RadioField,\
    BooleanField, SubmitField, IntegerField, FormField, validators
from wtforms.validators import Required

app = Flask(__name__)
Bootstrap(app)

@app.route('/', methods=('GET', 'POST'))
def index():
    #build up database table to send to index
    data = {}
    try:
        execfile("app/data.py",data)
    except:
        execfile("data.py",data)
    bevLU = data["Table"]["Beverage"]
    list =[]
    for key, value in data["Table"]["Location"].iteritems():
        temp = bevLU[int(value)]
        list += [[key,temp]]
    print list
    return render_template('index.html', x = list)
    

#if __name__ == '__main__':
    #create_app().run()
    #create_app().run(debug=True)
