from flask import Flask, render_template

# run command as below at the Terminal
# flask - -app main run

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
