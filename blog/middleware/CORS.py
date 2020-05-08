from django.utils.deprecation import MiddlewareMixin


class CORSMid(MiddlewareMixin):
    def process_response(self, request, response):
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Credentials"] = "true"
        response["Access-Control-Allow-Methods"] = "*"
        response["Access-Control-Allow-Headers"] = "Content-Type,Access-Token"
        response["Access-Control-Expose-Headers"] = "*"
        return response
