
# Import necessary libraries
from flask import Flask, request, render_template
from bs4 import BeautifulSoup
import requests

# Initialize the Flask application
app = Flask(__name__)

# Define the route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Define the route for analyzing the URL
@app.route('/analyze', methods=['GET', 'POST'])
def analyze():
    if request.method == 'POST':
        # Get the URL from the form data
        url = request.form['url']

        # Fetch the web page from the URL
        response = requests.get(url)

        # Parse the HTML content of the web page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract relevant information from the web page
        page_title = soup.title.string
        meta_tags = soup.find_all('meta')
        headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

        # Store the extracted information in a dictionary
        analysis_results = {
            'page_title': page_title,
            'meta_tags': meta_tags,
            'headings': headings
        }

        # Render the analysis results page
        return render_template('analysis.html', analysis_results=analysis_results)

    return render_template('analyze.html')

# Run the Flask application
if __name__ == '__main__':
    app.run()


This code implements the functionality described in the problem statement. It includes a home page (index.html) with a form for entering the URL, an analysis page (analysis.html) for displaying the analysis results, and the necessary Flask routes to handle the form submission and URL analysis. The code also utilizes the `BeautifulSoup` library to parse the HTML content of the web page and extract relevant information.

Please note that HTML files (index.html and analysis.html) are not included in this code as they are external files that need to be created separately. Additionally, the `requests` library needs to be installed before running the application.