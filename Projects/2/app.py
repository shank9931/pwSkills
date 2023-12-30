from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/api_data')
def api_data():
    # Define the URL of the API
    url = 'https://jsonplaceholder.typicode.com/posts'

    # Send a request to the API
    response = requests.get(url)

    # Get the JSON data from the response
    data = response.json()

    # Return the data to 'api_data.html' template
    return render_template('api_data.html', data=data)

if __name__ == "__main__":
    app.run(debug=True)
