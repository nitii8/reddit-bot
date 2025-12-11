import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Bot configuration settings"""
    REDDIT_CLIENT_ID = os.getenv('REDDIT_CLIENT_ID')
    REDDIT_CLIENT_SECRET = os.getenv('REDDIT_CLIENT_SECRET')
    REDDIT_USER_AGENT = os.getenv('REDDIT_USER_AGENT', 'RedditBot/1.0')
    REDDIT_USERNAME = os.getenv('REDDIT_USERNAME')
    REDDIT_PASSWORD = os.getenv('REDDIT_PASSWORD')
    
    SUBREDDIT_NAME = os.getenv('SUBREDDIT_NAME', 'moderation')
    CHECK_INTERVAL = int(os.getenv('CHECK_INTERVAL', '60'))
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    
    # Database
    DB_PATH = 'bot_data.db'
    
    # Moderation settings
    AUTO_MOD_ENABLED = os.getenv('AUTO_MOD_ENABLED', 'true').lower() == 'true'
    SPAM_THRESHOLD = int(os.getenv('SPAM_THRESHOLD', '5'))
    BAN_THRESHOLD = int(os.getenv('BAN_THRESHOLD', '3'))
    
if __name__ == '__main__':
    print('Configuration loaded successfully')
    print(f'Bot will monitor: {Config.SUBREDDIT_NAME}')
    print(f'Check interval: {Config.CHECK_INTERVAL}s')
