from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG']=True

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/', methods = ['POST'])
def validate_input():
    
    return render_template('base.html')

app.run()





