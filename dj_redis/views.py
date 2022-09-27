import time

from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

from dj_redis.utils import Redis
from django_redis import get_redis_connection
from django.core.cache import cache


# Create your views here.
def get_user(request):
    cache_data = Redis.get('user_data')
    if cache_data:
        return JsonResponse(cache_data, safe=False)

    time.sleep(5)
    cache_data = Redis.set('user_data', list(User.objects.values('username', 'is_superuser', 'is_active')))

    return JsonResponse(list(User.objects.values('username', 'is_superuser', 'is_active')), safe=False)


def get_redis(request):
    if cache.get('users'):
        print('Get from cache', cache.ttl('users'))
        data = cache.get('users')
        return HttpResponse(f'redis : {str(data[:])}')
    else:
        users = []
        data = User.objects.values('username', 'is_superuser')
        for i in data:
            cache.set('users', data)
        print('Get from db')

        return HttpResponse(f' db: {str(data[:])}')


def tearDown(self):
    get_redis_connection("default").flushall()
