from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@127.0.0.1/databasename'

db = SQLAlchemy(app)

rooms = [
    {
        'title': 'Entry',
        'flooring': 'Stone',
        'length': 5,
        'width': 5
    }
]

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db. relationship('Post', backref='title', lazy=True)

def __repr__(self):
    return f"User('{self.username}', '{self.email}','{self.image_file}')"

@app.route("/")
def hello():
    return render_template('home.html', rooms=rooms)

@app.route("/about")
def about():
    return "<h1>Fun Dungeon Time</h1>"

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'User created {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

if __name__ == '__main__':
    app.run(debug='True')