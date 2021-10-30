from flask import Flask
from categorizer_view import categorizer_view

app = Flask(__name__)

app.register_blueprint(categorizer_view)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()
