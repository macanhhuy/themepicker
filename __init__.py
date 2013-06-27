from flask import Flask
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__, static_folder='static', static_url_path='')
app.config["MONGODB_SETTINGS"] = {'DB': "my_tumble_log"}
app.config["SECRET_KEY"] = "KeepThisS3cr3t"

db = MongoEngine(app)

def register_blueprints(app):
    # Prevents circular imports
	from themepicker.views import posts
	from themepicker.admin import admin
	app.register_blueprint(posts)
	app.register_blueprint(admin)

register_blueprints(app)

if __name__ == '__main__':
    app.run(debug=True, use_debugger=True)