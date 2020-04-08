from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Home!!</h1>"

@app.route("/about")
def about():
    return "<h1>Fun Dungeon Time</h1>"

if __name__ == '__main__':
    app.run(debug='True')