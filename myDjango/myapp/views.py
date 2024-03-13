from django.shortcuts import render
from myapp.models import beer
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login 

def index(request):
    if request.method == "POST":
        data = request.POST
        print(data)
        new = beer(price = data["field1"] , taste = data["field2"] , turnover = data["field3"], description = data["field4"], main = data["field5"])
        new.save()
    res = beer.objects.all()
    print(res)
    return render(request,"index.html" , {"test":res})    

def main(request):
    if request.user.is_authenticated == True:
        data = beer.objects.all()
        return render(request, "main.html", {"res":data})
    else:
        return HttpResponse("Ошибка")

    
# Create your views here.

def regis(request):
    if request.method == "POST":
        data = request.POST
        user = User.objects.create_user (data["login"], data["mail"], data["password"]) 
        user.save()
        print(data)
    return render(request, "regis.html")


def auth(request):
    if request.method == "POST":
        data = request.POST
        user = authenticate(request , username = data["login"], password = data["password"])
        if user :
            login(request,user,)
        else:
            return HttpResponse("Не верный логин или пароль!!1!")
        
    print(request.user.is_authenticated)
    return render(request,"auth.html")


def present(request , myid):
    set = beer.objects.filter(id=myid)
    data = beer.objects.all()
    return render(request, 'card.html', {"set":set},)



 




    
    
    