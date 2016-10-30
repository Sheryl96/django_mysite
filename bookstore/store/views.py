from django.shortcuts import render
from .models import Books

def index(request):
    return render(request,'template.html')

def store(request):
    count=Books.objects.all().count()
    context={
        'count':count
    }
    request.session['location']="unknown"
    if request.user.is_authetiacted():
        request.session['location']="Earth"
    return render(request,'store.html',context)