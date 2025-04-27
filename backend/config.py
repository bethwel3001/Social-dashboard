import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-key-123')
    TWITTER_CLIENT_ID = os.getenv('TWITTER_CLIENT_ID')  # Twitter API client ID
    TWITTER_CLIENT_SECRET = os.getenv('TWITTER_CLIENT_SECRET') # Twitter API client secret