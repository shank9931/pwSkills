from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

@app.errorhandler(404)
def page_not_found(e):
    return "page not found", 404

@app.errorhandler(500)
def internal_server_error(e):
    return "internal server error", 500

if __name__ == "__main__":
    app.run()

