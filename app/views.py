from django.shortcuts import render

# Create your views here.
def conditions(request):
    d={'a':190,'b':120,'c':100}
    return render(request,'conditions.html',context=d)


def loop(request):
    d={'name':'sree'}
    return render(request,'loop.html',context=d)