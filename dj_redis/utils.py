import json

import redis

rds = redis.StrictRedis(port=6379, db=0)


class Redis:
    def set(key, value):
        data = json.dumps(value)
        rds.set(key, data)

        return True

    def get(key):
        data = rds.get(key)
        print(data)
        if not data:
            return None

        data = json.loads(data)

        return data