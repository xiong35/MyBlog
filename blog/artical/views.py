from django.http import JsonResponse
from django.views.generic import View
# Create your views here.


class Blog(View):

    def get(self, request):
        return JsonResponse({1: "12"})

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
