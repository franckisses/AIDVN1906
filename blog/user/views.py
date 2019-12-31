from django.shortcuts import render
from django.views import View
from django.http import JsonResponse

# Create your views here.

class UserRegisterView(View):
    """
    通过类视图来写view
    """
    def get(self,request):
        pass

    def post(self,request):
        print('test')
        return JsonResponse({
            'code':200
        })