import beanstalkc

beanstalk = beanstalkc.Connection(host='beanstalkd', port=11300)

while True:
    job = beanstalk.reserve()
    message = job.body
    print("Received message:", message)
    job.delete()
    