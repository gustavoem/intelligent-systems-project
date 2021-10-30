from flask import Flask
from categorizer_view import categorizer_view


def create_app():
    app = Flask(__name__)

    app.register_blueprint(categorizer_view)

    return app


app = create_app()

if __name__ == "__main__":
    app.run()

