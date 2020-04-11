import discogs_client

# Understand discogs api

# Create discogs connection
discogs = discogs_client.Client('SpinYoRecords')

# Send a query
results = discogs.search('Sunny Came Home',
                         type='release')

results[0].artists[0]
# Select a random result

# Select the link

# Return the link