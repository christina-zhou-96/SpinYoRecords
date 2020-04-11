from flask import Flask,redirect,request
from discogs import get_random_album

# Create app instance
app = Flask(__name__)

# Create homepage with button
@app.route("/")
def home():
    return """
    <html><body>
        <form action="/query">
            <input type='submit' value="I'm Feeling Lucky">
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