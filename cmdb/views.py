from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse
from  django.shortcuts import render


def index(request):
    #return HttpResponse(text)
    return render(request, 'hello.html')
def count(request):
    w=request.GET['text']
    count_=len(w)
    return render(request,'count.html',{"count_":count_})
