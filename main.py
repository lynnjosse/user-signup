from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG']=True

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/', methods = ['POST'])
def validate_input():


    username = str(request.form['username'])
    password1 = str(request.form['password1'])
    password2 = str(request.form['password2'])
    email = str(request.form['email'])

    if " " in username:
        username_error = "Please enter a username with no spaces."
    elif len(username) >20 or len(username) <3:
        username_error = "Usernames must be between 3 and 20 characters."
    else:
        username = username
        username_error = "" 

    if " " in password1:
        password1_error = "Please enter a password with no spaces."
    elif len(password1) >20 or len(password1) <3:
        password1_error = "Passwords must be between 3 and 20 characters."
    else:
        password1_error = ""        

    if password1 != password2:
        password2_error = "Password fields are not the same"
    else: password2_error = ''


    if " " in email:
        email_error = "That is not a valid email address"
    elif email == '':
        email_error = ""
    elif len(email) >20 or len(email) <6:
        email_error = "I don't like your email address because it is not between 7 and 20 characters."
    elif email.count('@') != 1:
        email_error = "That is not a valid email address"
    elif email.count('.') != 1:
        email_error = "That is not a valid email address"
    else:
        email_error = ""

    if email_error == "" == password1_error == password2_error == username_error:
        return redirect("/welcome?username={0}".format(username))

    
    return render_template('base.html', username_error=username_error, 
            password1_error = password1_error, password2_error = password2_error, 
            email_error = email_error, username = username , email = email)

@app.route('/welcome')
def welcome():
    username = request.args.get('username')
    return render_template('welcome.html', username = username)

app.run()





