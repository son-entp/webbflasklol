from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Fuck th cat, i haven't got any other words"

app.run()