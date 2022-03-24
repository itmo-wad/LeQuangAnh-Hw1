from flask import Flask, redirect, render_template, url_for
 
app= Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('user'))

@app.route('/user')
def user():
    return render_template("assigment_1.html")


app.run(host="localhost", port=5000, debug=True)