from django.http import *
from django.shortcuts import render
from .models import Task

# Create your views here.
donetasks = 0
forgottentasks = 0

def my(request):
    global list1
    global donetasks
    # if request.POST.get('done'):
    #     donetasks += 1
    #     z = list1[list1request.POST.get('done')]
    #     z.done = True

    global forgottentasks

    data = Task.objects.all()

    if request.POST.get('forgotten'):
        print(request.POST.get('forgotten'))
        for i in data:
            print(i.name)
            if i.name == request.POST.get('forgotten'):
                i.forgotten = True
                print(i)
                i.save()
                forgottentasks+=1
                break
    elif request.POST.get('done'):
        for i in data:
            if i.name == request.POST.get('done'):
                i.done = True
                i.save()
                donetasks+=1
                break
    elif request.POST.get('key'):
        variable1=True
        name=request.POST.get('key')
        for i in data:
            if  i.name==name:
                i.delete()
        t = Task(name=name)
        t.save()
    data=Task.objects.all()
    list1 = []
    for i in data:
        if not (i.done or i.forgotten):
            list1.append(i)
    return render(request, "index.html", context={"list": list1, "donetasks":donetasks, "forgottentasks":forgottentasks})


def test(request):
    if request.POST.get('key'):
        t = Task(name=request.POST.get('key'))
        t.save()
    return HttpResponse(request.POST.get('key', 'nope'))


def site(request):
    return render(request, 'mainpage.html')
