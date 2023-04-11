from api.v1.endpoints.fairytale import fairytale
from api.v1.endpoints.server import server
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(
    app=app,
    resources=r"/*",
    origins="http://localhost:3000",
    methods=["GET"]
)
app.register_blueprint(server, url_prefix='/server')
app.register_blueprint(fairytale, url_prefix='/fairytale')

if __name__ == 'main':
    app.run()
