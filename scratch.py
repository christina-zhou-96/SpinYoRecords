import discogs_client
from read_credentials import read_credentials
import random

# Understand discogs api

# Data structures
CREDENTIALS_FILE = 'discogs_api_key.txt'

# Create discogs connection
DEVELOPER_KEY = read_credentials(CREDENTIALS_FILE)

discogs = discogs_client.Client('SpinYoRecords',
                                user_token=DEVELOPER_KEY)

# Send a query
results = discogs.search(type='master'
                         ) # "Master' means unique release

# Select a random number
results_limit = 10000
album_position = random.randint(1, max(results_limit, results.count))

# Go to the album
album = results[album_position]

# Retrieve the album link
url = album.url

# Return the link