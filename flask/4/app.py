from flask import Flask, render_template_string, request


app1 = Flask(__name__)

@app1.route("/")
def index():
    return render_template_string('''<form method= "POST" action="/display">
                                  <input type = "text" name= "user_input" placeholder = "enter something">
                                  <input type = "submit" value= "Submit">
                                  </form>''')

@app1.route("/display", methods=["POST"])
def display():
    user_input = request.form.get("user_input")
    return f"You entered : {user_input}"

if __name__ == "__main__":
    app1.run()