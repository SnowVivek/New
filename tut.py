from flask import Flask, render_template 
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/First")
def firstpage ():
    return render_template('First.html')

app.run(debug=True)    