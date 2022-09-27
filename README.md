# Django Redis installation

[docs](https://github.com/jazzband/django-redis)
[Шпаргалка](https://habr.com/ru/post/204354/)

## install basic Django

### Caching settings
```python
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

...
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"
```

```shell
# redis commands command write on linux

redis-server start
redis-cli # enter to redis env
127.0.0.1:6379> ping  out>PONG  # write in console ping to test
keys * # show all keys
set key value # add single data
mset 
exit  # quit
````

> ex:
> ```
>    set test:1:string "my binary safe string" > OK
>    get test:1:string > "my binary safe string"
>    getset test:1:string "other value" > "my binary safe string"  
>    type test:1:string > string
>    set test:1:vlaue "487" > OK
>    rename test:1:vlaue test:1:value > OK
>    exists  test:1:vlaue > (integer) 0
>    exists test:1:value > (integer) 1
>    keys test:1:*                            
>        1) "test:1:string"                                             
>        2) "test:1:value" 
>    del test:1:value > (integer) 1
>    keys test:1:* > 1) "test:1:string" 
>````

> время жизни объекта.
> ```
>ttl test:1:string > (integer) -1
> expire test:1:string 6000 > (integer) 1
> ttl test:1:string > (integer) 5997
>```

more detail read on [Шпаргалка](https://habr.com/ru/post/204354/)...
