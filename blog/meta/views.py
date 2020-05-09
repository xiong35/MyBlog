
from django.http import JsonResponse
from django.views.generic import View

from .models import BlogMeta as BlogMetaModel

import json


class BlogMeta(View):

    def get(self, request):

        qs = BlogMetaModel.objects.all().values()
        if qs:
            return JsonResponse({'status': 200, 'data': list(qs)})
        return JsonResponse({"status": 404})
