from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, Email
from flask_bootstrap import Bootstrap

class Form(FlaskForm):
    name = StringField(label="Cardholder Name", validators=[DataRequired(), Email()])
    card = IntegerField(label="Credit Card Number", validators=[DataRequired(), Length(min=16, max=16)])
    expiration = DateField(label="Expiration Date", validators=[DataRequired(), Length(min=4, max=4)])
    csc = IntegerField(label="CSC Code", validators=[DataRequired(), Length(min=3, max=3)])
    submit = SubmitField(label="Submit")

app = Flask(__name__)
Bootstrap(app)

app.secret_key = "gfds4243ebgfd4134bdg68h24hb24n6"

@app.route("/", methods = ["GET", "POST"])
def home():
    form = Form()
    return render_template('index.html', form=form)

@app.route("/success")
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)