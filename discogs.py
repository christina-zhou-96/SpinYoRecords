import discogs_client
from read_credentials import read_credentials
import random

# Data structures
CREDENTIALS_FILE = 'discogs_api_key.txt'

# Create discogs connection
def _build_discogs_instance():
    DEVELOPER_KEY = read_credentials(CREDENTIALS_FILE)

    discogs = discogs_client.Client('SpinYoRecords',
                                    user_token=DEVELOPER_KEY)

    return discogs

# Send a query
def _query(discogs):
    
    # Select genres
    genre = ('Electronic', # yellow
             'Rock', # red
             'Jazz', # blue
             'Pop', # pink
             'Classical') # green

    # Select styles
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

    # Randomize sorting
    def __randomize_sorting(type):

        # Data structures
        # Possible values as noted in the official docs
        sorting_cats = ('year',
                        'title',
                        'format')

        sorting_order = ('asc',
                         'desc')

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

    results = discogs.search(type='master', # "Master' means unique release
                             sort=__randomize_sorting('sort'),
                             sort_order=__randomize_sorting('sort_order')
                             )
    return results

# Return a random album link
def _random_album_link(results):

    # Select a random number
    results_limit = 10000
    album_position = random.randint(1, results_limit)

    # Go to the album
    album = results[album_position]

    # Retrieve the album link
    discogs_url = "https://www.discogs.com/" # not sure why passing along the url attribute doesn't have this
    url = discogs_url + album.url

    # Return the link
    return url

# Outer function
def get_random_album():
    discogs = _build_discogs_instance()
    results = _query(discogs)
    random_album_link = _random_album_link(results)
    return random_album_link