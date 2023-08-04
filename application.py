import configparser
import os

from flask import Flask, render_template, request
import redis

application = Flask(__name__)

config_file = 'config.ini'
config = configparser.ConfigParser()
config.read(config_file)
host = os.environ.get('REDIS_HOST') or config.get('Redis', 'host')
pool = redis.ConnectionPool(host=host, port=6379, db=0)
redis = redis.Redis(connection_pool=pool)


@application.route("/")
def hello():
    return render_template('index.html')

def redis_str_to_int(string):
    return int(string.decode('utf-8'))

@application.route('/process', methods=['POST'])
def process():
    key = request.form.get('data')
    value = redis.get(key)
    if key and not value:
        redis.set(key, int(key) * 2)
    my_dict = {}
    for key in redis.scan_iter():
        my_dict[redis_str_to_int(key)] = redis_str_to_int(redis.get(key))
    return " all values: " + str(my_dict)

if __name__ == "__main__":
    application.debug = True
    application.run(host="0.0.0.0")