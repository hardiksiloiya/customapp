from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import ast
import urllib.request, json
import sys
sys.path.append('../')
from polls.models import user

def register(request):
    if request.method == 'POST':
        regobj = user
        regobj.name = request.POST["name"]
        regobj.age = request.POST["age"]
        regobj.password = request.POST["password"]
        regobj.location = request.POST["location"]
        regobj.gender = request.POST["gender"]
        regobj.family_type = request.POST["family_type"]
        regobj.login = request.POST["login"]
        regobj.ml_model = request.POST["ml_model"]

        regobj.save()

    return HttpResponse("success")

def login(request):
    if request.method == 'GET':
        i=1
        while(i<=user.objects.all().count()):
            obj = user.objects.get(id=i)
            if obj.name == request.GET["name"]:
                if obj.password == request.GET["password"]:
                    return HttpResponse("login successful")
                else:
                    return HttpResponse("invalid password")

        return HttpResponse("invalid name")

def profedit(request):
    if request.method == 'POST':

        updated_obj = user.objects.filter(id=request.POST["id"])
        for str in request.POST["queries"]:
            updated_obj[str] = request.GET[str]

        updated_obj.save()
        return HttpResponse("profile updated")

def viewprofile(request):
    if request.method == 'GET':
        obj = user
        i=1
        while(i<=user.objects.all().count()):
            obj = user.objects.get(id=i)
            if obj.name == request.GET["name"]:
                dict = {}
                dict["name"]=obj.name
                dict["age"]=obj.age
                dict["location"]=obj.location
                dict["family_type"]=obj.family_type
                dict["gender"]=obj.gender
                dict["login"]=obj.login

                json_file = json.dumps(dict)
                return JsonResponse(json_file)
        return HttpResponse("no records found")
