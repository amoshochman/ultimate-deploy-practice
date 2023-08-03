from flask import Flask

application = Flask(__name__)

@application.route('/')
def index():
    return 'Web App with Python Flask!'

@application.route('/hello')
def hello():
    return 'Hello World!'


if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run(host="0.0.0.0")