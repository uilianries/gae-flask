#################
#### imports ####
#################

from os.path import join, isfile

from flask import Flask, render_template, make_response, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_mail import Mail
from flask_uploads import UploadSet, IMAGES, configure_uploads
from flask_pagedown import PageDown
from flask_migrate import Migrate
from flask_httpauth import HTTPBasicAuth


################
#### config ####
################

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
mail = Mail(app)
pagedown = PageDown(app)
migrate = Migrate(app, db)
auth = HTTPBasicAuth()
auth_token = HTTPBasicAuth()

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "users.login"

# Configure the image uploading via Flask-Uploads
images = UploadSet('images', IMAGES)
configure_uploads(app, images)


from app.models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == int(user_id)).first()


####################
#### blueprints ####
####################

from app.users.views import users_blueprint
from app.recipes.views import recipes_blueprint
from app.recipes_api.views import recipes_api_blueprint

# register the blueprints
app.register_blueprint(users_blueprint)
app.register_blueprint(recipes_blueprint)
app.register_blueprint(recipes_api_blueprint)


############################
#### custom error pages ####
############################

from app.models import ValidationError


@app.errorhandler(ValidationError)
def bad_request(e):
    response = jsonify({'status': 400, 'error': 'bad request',
                        'message': e.args[0]})
    response.status_code = 400
    return response


@app.errorhandler(400)
def page_not_found(e):
    return make_response(jsonify({'error': 'Not found'}), 400)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


# @app.errorhandler(404)
# def not_found(e):
#     response = jsonify({'status': 404, 'error': 'not found', 'message': 'invalid resource URI'})
#     response.status_code = 404
#     return response


@app.errorhandler(403)
def page_not_found(e):
    return render_template('403.html'), 403


@app.errorhandler(410)
def page_not_found(e):
    return render_template('410.html'), 410
