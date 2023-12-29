# 1 : a dictionary that stores usernames and passowrds
# 2 : login route checking if provided username and passoword match an entry in the dictionary
# 3 : on matching log the user in


from flask import Flask, request, render_template
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key'

login_manager = LoginManager()
login_manager.init_app(app)

class User(UserMixin):
    def __init__(self, id):
        self.id = id

users = {'user1': 'password1', 'user2': 'password2'}

@login_manager.user_loader
def load_user(user_id):
    if user_id in users:
        return User(user_id)
    return None

@app.route("/")
def index():
    return render_template('index.html')
    
@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username= request.form.get('username')
        password = request.form.get('password')
        if username in users and users[username] == password:
            user = User(username)
            login_user(user)
            return render_template('login.html')
    return "invalid credentials"

@app.route('/protected')
@login_required
def protected():
    return "Protected page"

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return 'logged out!'

if __name__ == "__main__":
    app.run()