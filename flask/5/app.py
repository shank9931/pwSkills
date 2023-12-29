from flask import Flask, session, redirect, url_for, request
from markupsafe import escape

app = Flask(__name__)

# secret key
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/")
def index():
    if "username" in session:
        return "Logged in as %s" % escape(session['username'])
    return "You are not logged in"

@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        session["username"] = request.form["username"]
        return redirect(url_for('index'))
    return ''' 
            <form method="post">
                <p><input type=text name=username>
                <p><input type=submit value=Login>
            </form>
    '''

@app.route("/logout")
def logout():
    # remove the username from the session if it is there
    session.pop("username", None)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run()

