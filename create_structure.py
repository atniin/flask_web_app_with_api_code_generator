import os

ROUTES = """
import os
import importlib
from flask import Blueprint

routes_bp = Blueprint('routes_bp', __name__)

def register_blueprints(app):
    views_dir = os.path.join(os.path.dirname(__file__), 'views')
    api_dir = os.path.join(os.path.dirname(__file__), 'api')

    for method in ['get', 'post']:
        method_dir = os.path.join(views_dir, method)
        for filename in os.listdir(method_dir):
            if filename.endswith('.py') and not filename.startswith('__'):
                module_name = f"app.views.{method}.{filename[:-3]}"
                module = importlib.import_module(module_name)
                
                for attr_name in dir(module):
                    if attr_name.endswith('_bp'):
                        blueprint = getattr(module, attr_name)
                        routes_bp.register_blueprint(blueprint)

    for method in ['get', 'post']:
        method_dir = os.path.join(api_dir, method)
        for filename in os.listdir(method_dir):
            if filename.endswith('.py') and not filename.startswith('__'):
                module_name = f"app.api.{method}.{filename[:-3]}"
                module = importlib.import_module(module_name)
                
                for attr_name in dir(module):
                    if attr_name.endswith('_bp'):
                        blueprint = getattr(module, attr_name)
                        routes_bp.register_blueprint(blueprint)

    app.register_blueprint(routes_bp) 
"""

APP_INIT = """
import os
from flask import Flask
from dotenv import load_dotenv
from config import config 
from .routes import register_blueprints 

def create_app(config_name=None):
    load_dotenv()
    if config_name is None:
        config_name = os.getenv('FLASK_ENV', 'development')
        
    app = Flask(__name__)
    app.config.from_object(config[config_name]) 
    register_blueprints(app)  
    return app
"""

APP = """
import os
from app import create_app

app = create_app()

if __name__ == '__main__':
    debug_mode = os.getenv('FLASK_ENV', 'development') == 'development' 
    app.run(debug=debug_mode) 
"""

CONFIG = """
import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key') 
    DEBUG = os.getenv('FLASK_DEBUG', '0') == '1' 

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
}
"""

INDEX = """
from flask import Blueprint, render_template

get_index_bp = Blueprint('get_index_bp', __name__)

@get_index_bp.route('/', methods=['GET'])
def index():
    return render_template('index.html')
"""

INDEX_API = """
from flask import Blueprint, jsonify

api_get_index_bp = Blueprint('api_get_index_bp', __name__)

@api_get_index_bp.route('/api/', methods=['GET'])
def api_index():
    return jsonify({"message": "Hello from the API!"})
"""

INDEX_TEMPLATE = """
<!DOCTYPE html>
<html lang="et">

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Hello World</title>
</head>

<body>
  <h1>Hello World From Flask!</h1>
</body>

</html>
"""

REQUIREMENTS = """
Flask>=3.0.0
gunicorn
requests
python-dotenv
"""

GITIGNORE = """
__pycache__/
*.pyc
*.pyo
.vscode/
.idea/
*.log
*.egg-info/
dist/
build/
.env
docker-compose.override.yml
docker-compose.yml
Dockerfile
.dockerignore
*.pem
*.key
"""

README = """
# My App

## Description
This is my Flask App. 

### Prerequisites
See: requirements.txt 
"""

STRUCTURE = {
    'app': {
        '__init__.py': APP_INIT,
        'routes.py': ROUTES,
        'services': {
            '__init__.py': '',
        },
        'views': { # Separated by method and theme
            '__init__.py': '',
            'get': {
                '__init__.py': '',
                'index.py': INDEX
            },
            'post': {
                '__init__.py': '',
            }
        },
        'api': { # Separated by method and theme
            '__init__.py': '',
            'get': {
                '__init__.py': '',
                'index.py': INDEX_API
            },
            'post': {
                '__init__.py': '',
            }
        },
        'templates': {
            'index.html': INDEX_TEMPLATE,
        },
        'static': {
            'css': {}, 
            'js': {},  
            'images': {},                
        }
    },
    'config': {
        '__init__.py': CONFIG,
    },
    'README.md': README,
    'requirements.txt': REQUIREMENTS,
    '.gitignore': GITIGNORE,
    'app.py': APP, 
    '.env': 'FLASK_ENV=development'
}


def create_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)  
            create_structure(path, content) 
        else:
            with open(path, 'w') as f:
                f.write(content)


def main() -> None:
    create_structure(os.path.dirname(os.path.abspath(__file__)), STRUCTURE)


if __name__ == "__main__":
    main()
