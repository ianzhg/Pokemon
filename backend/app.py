from flask import Flask
from routes import api

# Initialize Flask app
app = Flask(__name__)
app.config["SECRET_KEY"] = "671f4ab58743d49d745784f0aee2a877f168360f"
app.config["MONGO_URI"] = "mongodb+srv://admin:admin@cluster0.wj4vxhv.mongodb.net/?retryWrites=true&w=majority"
app.register_blueprint(api)


if __name__ == "__main__":
    from routes import *
    app.run()

