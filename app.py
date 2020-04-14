from flask import Flask,redirect,request,render_template
from discogs import get_random_album

# Create app instance
app = Flask(__name__)

# Create homepage with button
@app.route("/")
def home():
    # Oh the horror of writing html!
    return render_template('home.html')

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

    genre = request.args.get("genre")
    style = request.args.get("style")
    return redirect(get_random_album(genre=genre,
                                     style=style))

# Run app
if __name__ == "__main__":
    app.run(debug=True,port=600)