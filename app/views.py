from django.shortcuts import render

# Create your views here.

def wish(request):
    d={'name':'NIKKY','age':15}
    return render(request,'wish.html',context=d)
