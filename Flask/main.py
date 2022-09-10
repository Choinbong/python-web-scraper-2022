from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", name="JH")  # {{name}} in a html file


@app.route("/search")
def hello():
    return render_template("search.html")


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)
