from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return

@app.route("/about")
def about():
    return

if __name__ == "__main__":
    app.run(debug=True)