
from django.http import JsonResponse
from django.views.generic import View

from .models import Blog as BlogModel
from .models import ArticalTag
from .models import Trap as TrapModel


class Blog(View):

    def get(self, request):

        get_id = request.GET.get('id', None)
        if get_id:
            qs = BlogModel.objects.filter(pk=get_id).values('content')
            return JsonResponse({'state': 200, 'content': list(qs)[0]})

        json_data = [
            {'id': b.id,
             'tags': [a.tag_name for a in b.tags.all()],
             'last_update':b.last_update,
             'headline':b.headline} for b in BlogModel.objects.prefetch_related('tags')
        ]
        return JsonResponse({'state': 200, 'data': json_data})

    def post(self, request):
        return JsonResponse({})


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
