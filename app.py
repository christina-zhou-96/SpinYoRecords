from flask import Flask,redirect
from discogs import get_random_album

# TODO: look at more advanced form builders

# Create app instance
app = Flask(__name__)

# Create homepage with button
@app.route("/")
def home():
    return """
    <html><body>
    <h2> Spin yo records </h2>
        <form action="/query">
            <input type='submit' value="I'm Feeling Lucky">
    </body></html>
    """

# Create ~secret~ about page.
@app.route("/about")
def about():
    return"""
    <html><body>
        <b>
        <a href="https://github.com/christina-zhou-96/SpinYoRecords">Code</a>
        </b>
    </body></html>
    """

# Backend query to discogs
@app.route("/query")
def link():
    # Scratch implementation
    return redirect(get_random_album())

# Run app
if __name__ == "__main__":
    app.run(debug=True,port=600)