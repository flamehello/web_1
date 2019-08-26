from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse
from  django.shortcuts import render
from cmdb .models import Gallery


def index(request):
    gall=Gallery.objects
    #return HttpResponse(text)
    return render(request, 'hello.html',{'gall_':gall})
def count(request):
    w=request.GET['text']
    count_=len(w)
    return render(request,'count.html',{"count_":count_})
