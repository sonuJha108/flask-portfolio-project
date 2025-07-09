from flask import Flask,render_template,redirect,request,url_for,flash,session
import uuid
import os

app = Flask(__name__)


app.secret_key = "maker-secret-key"

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/design")
def design():
    return render_template("design.html")

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/upload", methods=['GET','POST'])
def upload():
    if request.method == "POST":
        name = request.form.get("firstname")
        lastname = request.form.get("lastname")
        schoolname = request.form.get("schoolname")
        collegename = request.form.get("collegename")
        phonenumber = request.form.get("phonenumber")
        email = request.form.get("email")
        about = request.form.get("about")
        skill1 = request.form.get("skill1")
        skill2 = request.form.get("skill2")
        skill3 = request.form.get("skill3")
        skill4 = request.form.get("skill4")
        skill5 = request.form.get("skill5")

        key = uuid.uuid1()
        #images upload files
        img = request.files['dp']
        img.save(f"static/images/{img.filename}")
        img_new_name = f"{key}{img.filename}"
        os.rename(f"static/images/{img.filename}",f"static/images/{img_new_name}")

    return render_template('layout.html',dname=name,lname=lastname,img = img_new_name,sk1=skill1,sk2=skill2,sk3=skill3,sk4=skill4,ski5=skill5)

if __name__ == "__main__":
    app.run(debug=True)
