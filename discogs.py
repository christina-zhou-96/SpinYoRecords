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
    results = discogs.search(type='master'
                             ) # "Master' means unique release
    return results

# Return a random album link
def _random_album_link(results):
    # Select a random number
    results_limit = 10000
    album_position = random.randint(1, max(results_limit, results.count))

    # Go to the album
    album = results[album_position]

    # Retrieve the album link
    url = album.url

    # Return the link
    return url

# Outer function
def get_random_album():
    discogs = _build_discogs_instance()
    results = _query(discogs)
    random_album_link = _random_album_link(results)
    return random_album_link