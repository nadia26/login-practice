from flask import Flask,render_template,request,session
import functions

    
app=Flask(__name__)

@app.route("/login", methods=["GET", "POST"])
def login ():
    if request.method=="GET":
        return render_template('login.html')
    button = request.form["b"]
    if button == "Login":
        username = request.form["username"]
        password = request.form["password"]
        if functions.authenticate(username,password):
            session['username'] = username
            return  redirect(url_for('home'))
        else:
            return redirect(url_for('login'))
    if button == "Register":
        return redirect(url_for('register'))

@app.route("/register")
def register():
    if request.method=="GET":
        return render_template('register.html', message = "")
    elif request.form["b"] == "Register":
        password = request.form["password"]
        confirm = request.form["confirm_password"]
        if (password != confirm):
            return render_template('register.html', message = "passwords don't match")
        else:
            username = request.form["username"]
            if functions.check(username):
                return render_template('register.html', message = "Sorry, that username is already taken.")
            else:
                name = request.form["name"]           
                functions.add_user(username, name, password)
                return redirect(url_for('home'))

@app.route("/")
@app.route("/home")
def home():
    if 'username' not in session:
        return render_template('home.html',name=None)
    else:
        return render_template('home.html',name=session['username'])

@app.route("/s1")
def s1():
    if 'username' not in session:
        return redirect(url_for('home'))
    else:
        return render_template('s1.html', name=session['username'])

@app.route("/s2")
def s2():
    if 'username' not in session:
        return redirect(url_for('home'))
    else:
        return render_template('s2.html', name=session['username'])

@app.route("/logout")
def logout():
    session.pop("n",None)
    return redirect("/")


if __name__ == "__main__":
    app.debug=True
    app.run()
