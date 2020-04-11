import discogs_client
from read_credentials import read_credentials

# Understand discogs api

# Data structures
CREDENTIALS_FILE = 'discogs_api_key.txt'

# Create discogs connection
DEVELOPER_KEY = read_credentials(CREDENTIALS_FILE)

discogs = discogs_client.Client('SpinYoRecords',
                                user_token=DEVELOPER_KEY)

# Send a query
results = discogs.search('Sunny Came Home',
                         type='release')

results[0].artists[0]
# Select a random result

# Select the link

# Return the link