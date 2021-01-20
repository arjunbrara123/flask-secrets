from flask import Flask, render_template
from flask_wtf import FlaskForm
from werkzeug.utils import redirect
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired
from wtforms.widgets import PasswordInput
from flask_bootstrap import Bootstrap



class MyForm(FlaskForm):
    email = StringField(label='Email:', validators=[DataRequired()])
    password = PasswordField(label='Password :', validators=[DataRequired()])
    submit = SubmitField(label="Log In")

app = Flask(__name__)
app.secret_key = 'abc123'
Bootstrap(app)

@app.route("/")
def home():
    return render_template('index.html')


@app.route('/login', methods=('GET', 'POST'))
def login():
    form = MyForm()
    if form.validate_on_submit():
        if form.email.data == "admin@email.com" and form.password.data == "12345678":
            return redirect('/success')
        else:
            return redirect('/denied')
    return render_template("login.html", form=form)


@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/denied')
def denied():
    return render_template('denied.html')


if __name__ == '__main__':
    app.run(debug=True)
