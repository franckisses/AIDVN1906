from django.http import JsonResponse


def test(requeset):
    return JsonResponse({'code':200})

def index(request):
    pass