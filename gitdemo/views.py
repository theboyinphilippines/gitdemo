from django.http import HttpResponse


def index_view(request):
    return HttpResponse('注册成功')