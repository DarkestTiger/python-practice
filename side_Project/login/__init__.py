from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'kimchijeon pajeon gogijeon haemulpajeon gochujeon N makgeolli malgo soju'

    from .views import views
    from . import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    return app
