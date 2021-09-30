from django.shortcuts import render
from django.http import HttpResponse
from instructors.models import Instructor

# Create your views here.
def hello(request):
    return render(request, 'index.html')

def instructors_list(request):
    instructors = Instructor.objects.all()
    return render(request, 'instructors.html', {'instructors_list': instructors})

def hello_python(request):
    return render(request, 'python.html')

def http(request):
    response = render(request, 'http.html')
    response['Age'] = 2000
    response.status_code = 404
    return response

def articles_str(request, data):
    return HttpResponse('Hello articles +++ ' + data)

def sum_two(request, a, b):
    s = int(a) + int(b)
    return HttpResponse(s)
