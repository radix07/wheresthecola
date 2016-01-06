from flask import Flask, render_template, flash
from flask_bootstrap import Bootstrap
from flask_appconfig import AppConfig
from flask_wtf import Form, RecaptchaField
from wtforms import TextField, HiddenField, ValidationError, RadioField,\
    BooleanField, SubmitField, IntegerField, FormField, validators
from wtforms.validators import Required

def create_app(configfile=None):
    app = Flask(__name__)
    AppConfig(app, configfile)  # Flask-Appconfig is not necessary, but
                                # highly recommend =)
                                # https://github.com/mbr/flask-appconfig
    Bootstrap(app)

    # in a real app, these should be configured through Flask-Appconfig
    #app.config['SECRET_KEY'] = 'devkey'
    #app.config['RECAPTCHA_PUBLIC_KEY'] = \
        #'6Lfol9cSAAAAADAkodaYl9wvQCwBMr3qGR_PPHcw'

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
        
    return app

if __name__ == '__main__':
    #create_app().run()
    create_app().run(debug=True)
