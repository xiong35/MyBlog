
from django.http import JsonResponse
from django.views.generic import View

from .models import Blog as BlogModel
from .models import ArticalTag
from .models import Trap as TrapModel

import json


class Blog(View):

    def get(self, request):

        get_id = request.GET.get('id', None)
        if get_id:
            qs = BlogModel.objects.filter(pk=get_id).values('content')
            return JsonResponse({'status': 200, 'content': list(qs)[0]})

        json_data = [
            {'id': b.id,
             'tags': [a.tag_name for a in b.tags.all()],
             'last_update':b.last_update,
             'headline':b.headline} for b in BlogModel.objects.prefetch_related('tags')
        ]
        return JsonResponse({'status': 200, 'data': json_data})

    def post(self, request):

        info = json.loads(request.body)

        record = BlogModel(content=info.get('content'),
                           headline=info.get('headline'))
        record.save()

        tags = ArticalTag.objects.filter(tag_name__in=info.get('tags'))
        for tag in tags:
            record.tags.add(tag)
            tag.taged()

        return JsonResponse({'status': 200})


class Trap(View):

    def get(self, request):
        return JsonResponse({1: "12"})

    def post(self, request):
        return JsonResponse({})


class Tag(View):

    def get(self, request):
        return JsonResponse({1: "12"})

    def post(self, request):
        return JsonResponse({})
