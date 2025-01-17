from flask import Flask
from categorizer_view import categorizer_view


def create_app(is_testing=False):
    app = Flask(__name__)

    app.register_blueprint(categorizer_view)
    if is_testing:
        app.config['TESTING'] = is_testing
        app.testing = True

    return app


app = create_app()

if __name__ == "__main__":
    app.run()

