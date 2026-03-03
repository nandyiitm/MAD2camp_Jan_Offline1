import redis

r = redis.Redis(host="localhost", port=6379, decode_responses=True)

print("Number of keys:", r.dbsize())
print("Some keys:", r.scan(count=10)[1])