from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    second_name = db.Column(db.String(32), nullable=False)
    email = db.Column(db.Text(32), nullable=False)
    password = db.Column(db.Text(32), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<User %r>' % self.id


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/registration', methods=['POST', 'GET'])
def registration():
    if request.method == 'POST':
        name = request.form['name']
        second_name = request.form['second_name']
        email = request.form['email']
        password = request.form['password']

        user = User(name=name, second_name=second_name, email=email, password=password)

        try:
            db.session.add(user)
            db.session.commit()
            return redirect('/')
        except:
            return "При регистрации произошла ошибка!"
    else:
        return render_template('registration.html')


if __name__ == "__main__":
    app.run(debug=True)
