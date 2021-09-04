from flask import Flask, request
from datetime import datetime
import time

app = Flask(__name__)


@app.route("/status")
def status():
    return {
        "status": True,
        "name": "MyTestMessenger",
        "time": datetime.now().strftime("%Y.%m.%d %H:%M:%S")
    }

if __name__ == "__main__":
    app.run(debug=True)