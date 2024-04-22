from flask import Flask, request
import redis

app = Flask(__name__)
redis_client = redis.Redis(host='localhost', port=6380, db=0)

@app.route('/put_message', methods=['POST'])
def put_message():
    message = request.json.get('message')
    redis_client.rpush('queue', message)
    return "Message successfully added to the queue"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
