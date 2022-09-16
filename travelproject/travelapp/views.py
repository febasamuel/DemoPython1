from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def demo(request):

    return render(request, "index.html")
# def addition(request):
#     x = int(request.GET['num1'])
#     y = int(request.GET['num2'])
#     res = x+y
#     return render(request, "result.html", {'result': res})
# def about(request):
#     return render(request, "result.html")
#
# def contact(request):
#     return HttpResponse("hello i am contact")
