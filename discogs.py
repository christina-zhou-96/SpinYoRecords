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

    # Create query
    query = discogs.search(type='master')


    return query

# Get an album
def _random_album(query, discogs, genre):

    # Find total number of albums in db
    total_album_no = query.count

    if genre:
        # Stub: fake randomizer
        pass
    else:
        # Create a random id constrained by the total
        rand_id = random.randint(1, total_album_no)

        # Retrieve a random album with the random id
        album = discogs.master(rand_id)

        return album

# Get the album url
def _random_album_url(album):

    url = album.url

    return url

# Outer function
def get_random_album(genre=None):

    discogs = _build_discogs_instance()
    query = _query(discogs)
    random_album = _random_album(query,discogs,genre)
    random_album_url = _random_album_url(random_album)
    return random_album_url