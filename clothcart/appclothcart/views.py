from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import Cloth
from . forms import ClothForm




# Create your views here.



def cloths(request):
    database=Cloth.objects.all()

    return render(request,'intex.html',{'object':database})

def detail(request,cloth_id):
    cloth=Cloth.objects.get(id=cloth_id)

    return render(request,"details.html",{'cloth':cloth})


def addcloth(request):
    if request.method=="POST":
        head=request.POST.get('head')
        description = request.POST.get('description')
        year = request.POST.get('year')
        image = request.FILES['image']
        cloth=Cloth(head=head,description=description,year=year,image=image)
        cloth.save()

    return render(request,'add.html')

def update(request,id):
    cloth=Cloth.objects.get(id=id)
    form=ClothForm(request.POST or None,request.FILES,instance=cloth)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'form':form,'cloth':cloth})

def delete(request,id):
    if request.method=='POST':
        cloth=Cloth.objects.get(id=id)
        cloth.delete()
        return redirect('/')
    return render(request, 'delete.html')


