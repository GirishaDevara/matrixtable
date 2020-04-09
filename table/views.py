from django.shortcuts import render

from django.http import HttpResponse
import pdb


def table(request,val1,val2):
    l = []
    c = 1
    for r in range(val1):
        l1 = []
        for col in range(val2):
            l1.append(c)
            c += 1
        l.append(l1)
    return render(request,'mtable.html',{'l':l})

# def showform(request):
#     # pdb.set_trace()
#     if request.method == 'POST':
#         # pdb.set_trace()
#         # data = dict(request.POST)
#         data = {}
#         # print(data,data.get('name'))
#         data['name'] = request.POST.get('name')
#         return render(request,"sampleoutput.html",data)
#     else:
#         return render(request,"sample.html",{})

def showform(request):
    return render(request,'sample.html')

def showdata(request):
    data = {}
    data['fname'] = request.POST.get('fname')
    data['lname'] = request.POST.get('lname')
    data['email'] = request.POST.get('email')
    data['phone']  = request.POST.get('phone')
    data['imgurl'] = request.POST.get('imgurl')
    return render(request,"sampleoutput.html",data)

def  staticform(request):
    if request.method == "POST":
        data = {}
        data['fname'] = request.POST.get('fname')
        data['lname'] = request.POST.get('lname')
        data['email'] = request.POST.get('email')
        data['phone'] = request.POST.get('phone')
        data['imgurl'] = request.POST.get('imgurl')
        return render(request, "staticformOP.html", data)
    else:
        return render(request, 'staticformIP.html')

def grade(request):
    if request.method == "POST":
        mark = int(request.POST.get('marks'))
        return render(request, "gradescale.html", {'marks': mark})
    else:
        return render(request, "gradeinputdata.html")

def inher(request):
    if request.method == "POST":
        return render(request,'inheroutput.html',{'name':request.POST.get('name')})
    else:
        return render(request,'inher.html')

def home(request):
    return render(request,'home.html')

def contacts(request):
    return render(request,'contacts.html')

def homeinheritance(request):
    return render(request,'homeinher.html')

def contactform(request):
    return render(request,'contactsinher.html')