# Helper method to read credentials from an outside source
# so as to protect privacy

def read_credentials(CREDENTIALS_FILE):
    file = open(CREDENTIALS_FILE,
                mode='r')
    DEVELOPER_KEY = file.read()
    file.close()
    return DEVELOPER_KEY