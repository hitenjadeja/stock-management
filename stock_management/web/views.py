from django.http.response import HttpResponse


def home_page(request):
    return HttpResponse('<html><title>Home</title></html>')
