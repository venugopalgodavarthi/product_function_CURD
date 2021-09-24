from django.shortcuts import render,redirect
from django.http import HttpResponse
from online.forms import *
from online.models import * 
from django.contrib import messages

# Create your views here.


def itemsview(request):
    if request.method=='POST':
        form = itemsform(request.POST)
        if form.is_valid():
            form.save()
        
    form = itemsform
    return render(request,'registeritems.html',{'items':form})

def productview(request):
    if request.method=='POST' and request.FILES:
        form1 = productform(request.POST,request.FILES)
        print(form1)
        if form1.is_valid():
            form1.save()
            messages.success(request,"product is created")
        else:
            messages.error(request,"product is not created")
    form1 = productform()
    return render(request,'registeritems.html',{'product':form1})

def productdetails(request):
    res=productmodel.objects.all()
    return render(request,"details.html",{'res':res})

def productmodify(request,pk):
    if request.method=='POST' or request.FILES:
        var = productmodel.objects.get(id=pk)
        form1 = productform(request.POST, request.FILES, instance=var)
        if form1.is_valid():
            print("hai")
            form1.save()
            messages.success(request,'your product is modified')
        else:
            messages.error(request,'your product data is not modified')

    res1=productmodel.objects.get(id=pk)
    return render(request,'modify.html',{'res':res1})


def productdelete(request,pk):
    res= productmodel.objects.filter(id=pk).delete()
    res= productmodel.objects.all()
    return render(request,'delete.html',{'res':res})



'''
def productmodify(request,pk):  
    if request.method=='POST' or request.FILES:
        res1 =productmodel.objects.get(id=pk)
        res1.pname = request.POST['pname']
        res1.pdesc = request.POST['pdesc']
        res1.pprice = request.POST['pprice']
        res1.pdiscount = request.POST['pdiscount']
        res1.ppic = request.FILES['ppic']
        res1.save()   
        print("hai") 
    res1=productmodel.objects.get(id=pk)
    return render(request,"modify.html",{'res':res1})
'''