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

    if genre or style:

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
    if genre or style:

        # Return a random album link

        # Select a random number, given the max of 10,000
        query_limit = 9999
        album_position = random.randint(0, query_limit)
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
    if genre or style:
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