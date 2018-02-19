##########################################################
#
# This is a sample flask.cfg for developing the Flask Recipe App.
#
##########################################################
import os


# grab the folder of the top-level directory of this project
BASEDIR = os.path.abspath(os.path.dirname(__file__))
TOP_LEVEL_DIR = os.path.abspath(os.curdir)

# Update later by using a random number generator and moving
# the actual key outside of the source code under version control
SECRET_KEY = 'cUyf7aIXbpPKZ3Uxcic139jc0K4t82YZ'
WTF_CSRF_ENABLED = True
DEBUG = False

# SQLAlchemy
SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
SQLALCHEMY_TRACK_MODIFICATIONS = True

# Bcrypt algorithm hashing rounds
BCRYPT_LOG_ROUNDS = 15

# Uploads
UPLOADS_DEFAULT_DEST = TOP_LEVEL_DIR + '/app/static/img/'
UPLOADS_DEFAULT_URL = 'http://localhost:5000/static/img/'

UPLOADED_IMAGES_DEST = TOP_LEVEL_DIR + '/app/static/img/'
UPLOADED_IMAGES_URL = 'http://localhost:5000/static/img/'

SESSION_TYPE = 'filesystem'
