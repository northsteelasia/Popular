from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/learn")
def learn():
    return render_template("learn.html")


@app.route("/learn/lesson1")
def lesson1():
    return render_template("lesson1.html")

@app.route("/learn/lesson2")
def lesson2():
    return render_template("lesson2.html")


if __name__ == "__main__":
    app.run(debug=True)