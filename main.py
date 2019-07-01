from flask import Flask, request, render_template

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/", methods=['POST'])
def welcome():
    username = request.form['username']
    password = request.form['password']
    verify_pw = request.form['verify_pw']
    add_email = request.form['email']
    un_error = ""
    pw_error = ""
    pwvr_error = ""
    em_error = ""

    valid = True
    if len(username) < 3 or len(username) > 20 or " " in username:
        un_error = "Must contain 3 to 20 characters"
        valid = False
    if len(password) < 3 or len(password) > 20 or " " in password:
        pw_error = "Must contain 3 to 20 characters"
        valid = False
    if password != verify_pw:
        pwvr_error = "Passwords do not match"
        valid = False
    if len(add_email) != 0:
        if len(add_email) < 3 or len(add_email) > 20 or " " in add_email or add_email.count(".") != 1 or add_email.count("@") != 1:
            em_error = "Email not valid"
            valid = False
    
    if valid == False:
        return render_template('index.html', username=username, email=add_email, un_error=un_error, pw_error=pw_error, pwvr_error=pwvr_error, em_error=em_error)

    return render_template('welcome.html', username=username)
app.run()    