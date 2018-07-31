import os

THIS_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__)))

DB_PATH = os.getenv('CAPE_USERDB_SQLITE_PATH', os.path.join(THIS_FOLDER, 'storage', 'capeusers.sqlite'))

DEFAULT_EMAIL = "answer@questions.mail"
DEFAULT_RESPONSE = "I'm sorry, we couldn't find a response"
DEFAULT_THRESHOLD = "MEDIUM"
