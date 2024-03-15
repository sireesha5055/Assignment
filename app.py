from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
from models import User
from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db.init_app(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        age = request.form['age']
        dob_str = request.form['dob']

        # Get the date of birth as a string
        dob = datetime.strptime(dob_str, '%Y-%m-%d').date()

        # Convert the string to a date object
        user = User(name=name, email=email, age=age, dob=dob)

        # Use User directly
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('index.html')


@app.route('/display_users')
def display_users():
    # Fetch all users from the database
    users = User.query.all()
    return render_template('users.html')


if __name__ == '__main__':
    app.run(debug=True)
