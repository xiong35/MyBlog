
from django.http import JsonResponse
from django.views.generic import View

from .models import Blog as BlogModel
from .models import ArticalTag
from .models import Trap as TrapModel
from meta.models import BlogMeta

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

import json


def update_meta():
    artical_model = BlogMeta.objects.filter(key__contains='文章').first()
    if artical_model:
        artical_model.update()


class Blog(View):

    @method_decorator(cache_page(60*5))
    def get(self, request):
        print('\n\n\nin\n\n')
        get_id = request.GET.get('id', None)
        if get_id:
            qs = BlogModel.objects.filter(pk=get_id).values('content')
            if qs:
                return JsonResponse({'status': 200, 'content': list(qs)[0]})
            return JsonResponse({"status": 404})

        json_data = [
            {'id': b.id,
             'tags': [a.tag_name for a in b.tags.all()],
             'last_update':b.last_update,
             'headline':b.headline} for b in BlogModel.objects.prefetch_related('tags')
        ]
        # TODO move sort to front

        json_data = sorted(
            json_data, key=lambda i: i['last_update'], reverse=True)

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

        update_meta()
        return JsonResponse({'status': 200})


class Trap(View):

    def get(self, request):

        get_id = request.GET.get('id', None)
        if get_id:
            qs = TrapModel.objects.filter(pk=get_id).values().first()
            if qs:
                return JsonResponse({'status': 200, 'data': qs})
            return JsonResponse({"status": 404})

        json_data = [
            {'id': b.id,
             'tags': [a.tag_name for a in b.tags.all()],
             'last_update':b.last_update,
             'context':b.context,
             'problem':b.problem} for b in TrapModel.objects.prefetch_related('tags')
        ]
        # TODO move sort to front

        json_data = sorted(
            json_data, key=lambda i: i['last_update'], reverse=True)

        return JsonResponse({"status": 200, "data": json_data})

    def post(self, request):

        json_data = json.loads(request.body)

        tag_names = json_data.get("tag_names")
        context = json_data.get("context")
        problem = json_data.get("problem")
        solution = json_data.get("solution")

        record = TrapModel(context=context, problem=problem, solution=solution)
        record.save()
        tags = ArticalTag.objects.filter(tag_name__in=tag_names)

        for tag in tags:
            record.tags.add(tag)
            tag.taged()

        update_meta()
        return JsonResponse({"status": 200})


class Tag(View):

    def get(self, request):
        qs = ArticalTag.objects.values()
        return JsonResponse({"status": 200, "data": list(qs)})

    def post(self, request):
        tag_names = json.loads(request.body).get("tag_names")
        for tag_name in tag_names:
            tag = ArticalTag(tag_name=tag_name)
            tag.save()

        return JsonResponse({"status": 200})
