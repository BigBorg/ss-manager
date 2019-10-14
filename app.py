# encoding:utf8
from flask import Flask, render_template
from modules.authentication import bp as authentication
from modules.shadow import bp as shadow


def create_app():
    app:Flask = Flask(__name__)
    app.config.from_pyfile("settings.py")
    app.register_blueprint(authentication)
    app.register_blueprint(shadow)

    @app.route("/", methods=["GET"])
    def index():
        return render_template("index.html")

    return app


app = create_app()

if __name__ == "__main__":
    print(app.url_map)
    app.run(host="127.0.0.1", port=8888)
