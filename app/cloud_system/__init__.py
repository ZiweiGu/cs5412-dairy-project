from flask import Blueprint

# Define a Blueprint for this module (mchat)
cloud_system = Blueprint('cloud_system', __name__, url_prefix='/',static_folder='static',template_folder='templates')

# Import all controllers
from .controllers.controller import *