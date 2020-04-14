import discogs_client
from read_credentials import read_credentials
import random

# Data structures
CREDENTIALS_FILE = 'discogs_api_key.txt'

# Possible values as noted in the official docs
sorting_cats = ('year',
                'title',
                'format')

sorting_order = ('asc',
                 'desc')

# Create discogs connection
def _build_discogs_instance():

    DEVELOPER_KEY = read_credentials(CREDENTIALS_FILE)

    discogs = discogs_client.Client('SpinYoRecords',
                                    user_token=DEVELOPER_KEY)

    return discogs

# Send a query
def _query(discogs, genre, style):

    # Two different ways to build queries: one with and one without drilldown
    drilldown = genre or style

    if drilldown:

        # Randomize sorting
        def __randomize_sorting(type):

            # Randomize sorting category.
            def ___get_random_sort():
                return random.choice(sorting_cats)

            # Randomize way it's sorted (ascending or descending.)
            def ___get_random_sort_order():
                return random.choice(sorting_order)

            if type == 'sort':
                ___get_random_sort()
            if type == 'sort_order':
                ___get_random_sort_order()

        # These queries will be capped at 10,000

        # Unfortunately, running `search` with a None argument doesn't work,
        # so have to break it down as below.
        if genre:

            query = discogs.search(type='master',
                                   sort=__randomize_sorting('sort'),
                                   sort_order=__randomize_sorting('sort_order'),
                                   genre=genre
                                   )

        if style:

            query = discogs.search(type='master',
                                   sort=__randomize_sorting('sort'),
                                   sort_order=__randomize_sorting('sort_order'),
                                   style=style
                                   )

    else:
        # Create query
        query = discogs.search(type='master') # "Master' means unique release

    return query

# Get an album
def _random_album(query, discogs, genre, style):

    # Find total number of albums in db
    total_album_no = query.count

    # Two different ways to get an album: one with and one without drilldown
    drilldown = genre or style

    if drilldown:

        # Return a random album link

        # Select a random number, given either 10,000 or the lower number
        # of releases in this genre (for instance, Shoegaze only has about 5000
        # releases, so 5000 would be the constraint in this case)
        query_limit = 9999
        album_position = random.randint(0, min(total_album_no,query_limit))
        # Go to the album
        album = query[album_position]

    else:
        # Create a random id constrained by the total
        rand_id = random.randint(1, total_album_no)

        # Retrieve a random album with the random id
        album = discogs.master(rand_id)

    return album

# Get the album url
def _random_album_url(album,genre,style):

    # Two different ways to get a url: one with and one without drilldown
    drilldown = genre or style

    if drilldown:
        url = "https://www.discogs.com/" + album.url
    else:
        url = album.url

    return url

# Outer function
def get_random_album(genre=None,style=None):

    discogs = _build_discogs_instance()
    query = _query(discogs,genre,style)
    random_album = _random_album(query,discogs,genre,style)
    random_album_url = _random_album_url(random_album,genre,style)
    return random_album_url