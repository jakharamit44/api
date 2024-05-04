# Telegram API ID and Hash
API_ID = int("telegram_api_id")
API_HASH = "telegram_api_hash"

# Bot which will handle users commands
MAIN_BOT_TOKEN = "main_bot_token"

LOGGER_BOT_TOKEN = "logger_bot_token"

# Bot tokens for STORAGE_CHANNEL_1, they all must be admin in the channel
UPLOADER_BOTS_1 = ["7092415941:AAE6fvm2DAANcHgCFuIFQbrb2JUqPaRtqog", "7005857065:AAEwa-AaD-OLIdjLziCN-mvmMosPCLaIBKA", "6785391905:AAFTloV690JYo6TQMIUlQXa8pQ0kEozgtpU"]

# Bot tokens for STORAGE_CHANNEL_2, they all must be admin in the channel
UPLOADER_BOTS_2 = ["7167715976:AAE7D6nkm2ELCgAsXK7IGUOlpkGFxdad4Vo", "6751989885:AAEIxK_wQSmbk3UgeT3Y6zxGmCgeUF3HNMA", "bot_token6"]

# Telegram Channel ID where videos will be stored
VIDEO_STORAGE = -1002133672128
# Telegram Channel ID where logs will be stored
LOGGER_CHANNEL = -1002146191116
# Telegram Channel ID where m3u8 file will be stored
STORAGE_CHANNEL_1 = -1002091415759
STORAGE_CHANNEL_2 = -1002091415759

# Max no. of tasks to run simultaneously
MAX_ACTIVE_TASKS = 5

# Max no. of tasks a user can run simultaneously
MAX_USER_CONCURRENT_TASKS = 3

# No. of simulataneous uploaders to run per task for .ts file upload
NO_OF_UPLOADERS = 5

# In MB (MegaBytes). Size of each segment uploaded to telegram. Must be less than 10 MB
SEGMENT_SIZE = 2

# Telegram User ID of the bot owner
OWNER_ID = 1234567890

# Domain name of the website where the stream api is hosted
WEBSITE_DOMAIN = "https://stream.mywebsite.com"

# MongoDB Database URL
MONGO_DB_URL = "mongodb+srv://database:pass@cluster0.gdsgfg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Playerx.stream Login details
PLAYERX_EMAIL = "your_email@gmail.com"
PLAYERX_PASSWORD = "your_password"
PLAYERX_API_KEY = "your_api"
