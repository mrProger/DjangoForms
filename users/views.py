from django.shortcuts import render
from django.http import HttpResponse

def page(request):
    return render(request, 'page.html')

def postperson(request):
    name = request.POST.get('name')
    age = request.POST.get('age')
    return HttpResponse(f'Name - {name}<br>Age - {age}')