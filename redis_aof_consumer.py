import redis

redis_client = redis.Redis(host='localhost', port=6380, db=0)

while True:
    message = redis_client.blpop('queue')
    print("Received message:", message[1].decode())