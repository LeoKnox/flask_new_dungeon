from flask import Flask, render_template

app = Flask(__name__)

rooms = [
    {
        'title': 'Entry',
        'flooring': 'Stone',
        'length': 5,
        'width': 5
    }
]

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