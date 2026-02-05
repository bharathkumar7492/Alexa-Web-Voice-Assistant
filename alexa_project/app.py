from flask import Flask, render_template
from alexa import run_alexa

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", command="", response="")

@app.route("/listen", methods=["POST"])
def listen():
    response = run_alexa()
    return render_template("index.html",
                           command="Voice command detected",
                           response=response)

if __name__ == "__main__":
    app.run(debug=False)
