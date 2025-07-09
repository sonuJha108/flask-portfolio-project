from flask import Flask,render_template,redirect,request,url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/design")
def design():
    return render_template("design.html")

@app.route("/upload")
def upload():
    if request.method == "POST":
        pass

if __name__ == "__main__":
    app.run(debug=True)
