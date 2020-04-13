from flask import Flask,redirect,request
from discogs import get_random_album

# TODO: look at more advanced form builders


# Stub: Select genres
genres = ('Electronic',  # yellow
          'Rock',  # red
          'Jazz',  # blue
          'Pop',  # pink
          'Classical')  # green

# Stub: Select styles
styles = ('Ambient',
          'Drone',
          'Shoegaze',
          'Pop Rock',
          'Post Rock',
          'Hard Rock',
          'Prog Rock',
          'Black Metal',
          'Folk, World, & Country',
          'RnB/Swing',
          'Modern'
          )

# Create app instance
app = Flask(__name__)

# Create homepage with button
@app.route("/")
def home():
    # Currently list of genres is hardcoded in
    return """
    <html><body>
    <h2> Spin yo records </h2>
        <form action="/query">
            <input type='submit' value="I'm Feeling Lucky">
        </form>
        <form action="/query">
            <input type='submit' name='genre' value="Electronic">
            <input type='submit' name='genre' value="Rock">
            <input type='submit' name='genre' value="Jazz">
            <input type='submit' name='genre' value="Pop">
            <input type='submit' name='genre' value="Classical">
        </form>
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

    genre = request.args.get("genre")
    return redirect(get_random_album(genre=genre))

# Run app
if __name__ == "__main__":
    app.run(debug=True,port=600)