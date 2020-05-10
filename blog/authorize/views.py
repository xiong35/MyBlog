from django.http import JsonResponse
from django.views.generic import View

from .models import Visiter

import time
import hashlib
import json
import datetime as dt


class Authorize(View):

    def get(self, request):
        # remote_addr = request.META.get("REMOTE_ADDR")
        # agent = request.META.get("HTTP_USER_AGENT")
        # if not agent:
        #     agent = 'none'
        # token = gen_token(remote_addr, agent)

        return JsonResponse({1: 2})

    def post(self, request):
        info = json.loads(request.body)

        token = info.get('token')

        now = dt.datetime.now()

        qs = Visiter.objects.filter(token=token).filter(
            expire__lt=now).first()

        if not qs:
            remote_addr = request.META.get("REMOTE_ADDR")
            agent = request.META.get("HTTP_USER_AGENT")
            if not agent:
                agent = 'none'
            token = gen_token(remote_addr, agent)

            qs = Visiter(token=token, expire=now + dt.timedelta(days=1))

        password = info.get('password')
        if password:
            if hashlib.new("md5", password.encode('utf-8')).hexdigest() == 'a14068983c35ab6018046087da23fd4c':
                qs.authority = 'root'

        qs.save()

        return JsonResponse({'status': 200})


def gen_token(remote_addr, agent):
    t = str(time.time())
    token = hashlib.new(
        'md5', (t+remote_addr+agent).encode('utf-8')).hexdigest()
    print(token)
    return token


def gen_auth_code(request):
    return JsonResponse({1: 'asd'})
