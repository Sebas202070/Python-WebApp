from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")
@app.route("/About")
def about():
       return render_template("about.html")
app.run(debug=True)