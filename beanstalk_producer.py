from flask import Flask, request
import beanstalkc

app = Flask(__name__)
beanstalk = beanstalkc.Connection(host='localhost', port=11300)

@app.route('/put_message', methods=['POST'])
def put_message():
    message = request.json.get('message')
    beanstalk.put(message)
    return "Message successfully added to the queue"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)
