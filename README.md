Get a random record! <br>

Try it out at <b> https://spinyorecord.herokuapp.com/ </b> <br>

<b>
Notes
</b>

<br>

This goes into Discogs, which is a pretty good music website, and just picks out a random album for you.

Not much else to say here...


<b>
Resources
</b>

<br>

Local app <br>
1. Make a Flask app <br>
https://runestone.academy/runestone/books/published/thinkcspy/WebApps/07-InputForAFlaskWebApplication.html <br>

Deployment <br>
1. Overview to deploy with Heroku <br>
which sounds cuter and easier than Amazon or Google <br>
https://pythonhow.com/deploying-your-web-application-to-the-cloud/ <br>

2. Generating a requirements file <br>
https://stackoverflow.com/questions/40192651/django-pip-freeze-results-in-empty-file <br>

3. The official Windows help <br>
Notice the special Windows procfile... <br>
https://devcenter.heroku.com/articles/getting-started-with-python#deploy-the-app <br>

4. Make a Procfile with Waitress <br>
https://books.google.com/books?id=cVlPDwAAQBAJ&pg=PT282&lpg=PT282&dq=%22waitress%22+procfile&source=bl&ots=xNJYeoYq9_&sig=ACfU3U1aUYxH6Zjxy5pi-jXDJdf4CZF_2w&hl=en&sa=X&ved=2ahUKEwioxOPcitzoAhWCl3IEHSGsAwoQ6AEwBnoECAkQKQ#v=onepage&q=%22waitress%22%20procfile&f=false
<br> If you're on Windows, you can't use gunicorn, which is what the tutorial
wants you to use. (The tutorial does have an example Windows procfile, but
that's only applicable for local use.) <br>

Connect to Discogs <br>

1. Overview of steps to use Discogs API <br>
https://www.discogs.com/developers#page:home,header:home-quickstart <br>

2. Get a developer token <br>
https://auth.discogs.com/login?service=https%3A//www.discogs.com/login%3Freturn_to%3D%252Fsettings%252Fdevelopers%253F&nologin=1 <br>

3. Understanding what's possible with client object, search object <br>
https://github.com/discogs/discogs_client<br>

4. More on search object <br>
https://www.discogs.com/developers#page:database,header:database-search<br>

5. More on release object <br>
https://www.discogs.com/developers#page:database,header:database-artist-releases<br>

6. More on master object <br>
https://www.discogs.com/developers#page:database,header:database-master-release

7. Tip from radum on discogs forums <br>
https://www.discogs.com/forum/thread/815327?page=1#8095702 <br>

<b>Contributions</b> <br>
Select genre: I'm thinking about selecting by my favorite genres (in discogs.py).
However, I wonder if that takes away from the random/discovery element.
Also, I don't know how to make more complicated forms, and I wouldn't know
how to make them look attractive but still retain the sparse look.

No Youtube playlist?: Some of these albums don't have a readily accessibly
Youtube playlist in the sidebar. Personally, I then Google the albums and find
at least one song by the same artist to play. So, I think these albums are still
valid, and that the current method kind of negates the one click "spin the record"
experience. Possibly? link to their SoundCloud, YT, or BandCamp presence.

<b>Other small fixes</b> <br>
Requirements: The requirements file is bloated because I didn't use a different
virtual env.

