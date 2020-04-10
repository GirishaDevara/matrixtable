from django.shortcuts import render, redirect, get_object_or_404
from table.models import Item, employee
from django.http import HttpResponse
# import pdb

def index(request):
    all_items = Item.objects.all()
    return render(request,'index.html',{'all_items':all_items})

def contacts(request):
    return render(request,'contacts.html')
def about(request):
    return render(request,'about.html')

def edititem(request,id):
    item = Item.objects.get(id=id)
    if request.method == 'POST':
        name = request.POST.get('name')
        cost = request.POST.get('cost')
        imgurl = request.POST.get('imgurl')
        description = request.POST.get('description')
        item.name  = name
        item.cost = cost
        item.image_url = imgurl
        item.description = description
        item.save()
        return redirect('/item')
    else:
        return render(request,'edititem.html',{'item':item})

def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        cost = request.POST.get('cost')
        imgurl = request.POST.get('imgurl')
        description =request.POST.get('description')
        item = Item(name = name, cost = cost, image_url =  imgurl, description = description)
        item.save()
        return redirect('/item')
    else:
        return render(request,'createitem.html')

def delete(request,id):
    obj = get_object_or_404(Item, id=id)
    obj.delete()
    return redirect('/item')
