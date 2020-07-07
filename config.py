import os

basedir = os.path.abspath(os.path.dirname(__file__))
SECRET_KEY="jhsdajusgduyaygfshfgjadbvnxcbvhgdesftgyg"
DEBUG=True
EXPECTED_DB_PATH = 'blog.db'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, EXPECTED_DB_PATH)
SQLALCHEMY_TRACK_MODIFICATIONS = False