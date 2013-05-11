import redis 

rs = redis.Redis()
rs.publish("testChannel", "Hello world from a Redis publisher ...")
