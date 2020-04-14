from flask import Flask,redirect,request
from discogs import get_random_album

# Data structures

header_html = """
<h2> Spin yo records </h2>"""

all_form_html = """
        <form action="/query">
            <input type='submit' value="I'm Feeling Lucky">
        </form>
        """

genres_form_html = """
        <form action="/query">
            <input type='submit' name='genre' value="Electronic">
            <input type='submit' name='genre' value="Rock">
            <input type='submit' name='genre' value="Jazz">
            <input type='submit' name='genre' value="Pop">
            <input type='submit' name='genre' value="Classical">
        </form>
        """

# Folk is Folk, World, & Country, but the full phrase doesn't work with discogs api
styles_form_html = """
        <form action="/query">
            <input type='submit' name='style' value="Ambient">
            <input type='submit' name='style' value="Drone">
            <input type='submit' name='style' value="Shoegaze">
            <input type='submit' name='style' value="Pop Rock">
            <input type='submit' name='style' value="Post Rock">
            <input type='submit' name='style' value="Hard Rock">
            <input type='submit' name='style' value="Prog Rock">
            <input type='submit' name='style' value="Black Metal">
            <input type='submit' name='style' value="Folk">
            <input type='submit' name='style' value="Modern">
        </form>
        """

# Create app instance
app = Flask(__name__)

# Create homepage with button
@app.route("/")
def home():
    # Currently list of genres is hardcoded in
    return """
            <html><body>""" \
           + header_html \
           + all_form_html \
           + genres_form_html \
           + styles_form_html + \
           """
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
    style = request.args.get("style")
    return redirect(get_random_album(genre=genre,
                                     style=style))

# Run app
if __name__ == "__main__":
    app.run(debug=True,port=600)