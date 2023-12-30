from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/scrape')
def scrape():
    # Define the URL of the site
    url = 'https://www.youtube.com/'

    # Send a request to the website
    r = requests.get(url)

    # Get the HTML content of the page
    html_content = r.text

    # Create a BeautifulSoup object and specify the parser
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract information
    data = soup.find_all('a')

    # Return the scraped data
    return render_template('scrape.html', data=data)

if __name__ == "__main__":
    app.run(debug=True)
