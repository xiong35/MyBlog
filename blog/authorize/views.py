from django.http import JsonResponse
from django.views.generic import View
# Create your views here.


class Authorize(View):

    def get(self, request):
        return JsonResponse({1: "12"})

    def post(self, request):
        return JsonResponse({})


def gen_auth_code(request):
    return JsonResponse({1:'asd'})
