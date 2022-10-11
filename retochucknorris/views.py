import re
import json
import os
from psycopg2 import Date
import pyrebase
import requests
from urllib import request, response
from django.shortcuts import redirect, render
from django.contrib import auth
from supabase import create_client, Client


url_api = "https://api.chucknorris.io/jokes/random"
user = None

url: str = "https://vjvkzcmihnvzopcxzsme.supabase.co"
print(url)
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InZqdmt6Y21paG52em9wY3h6c21lIiwicm9sZSI6ImFub24iLCJpYXQiOjE2NjUzNzAxMzIsImV4cCI6MTk4MDk0NjEzMn0.LH6Y3TO-X-bqAroLq0y_45FVMmCLXA54GfwAlSG-XkA"
print(key)
supabase: Client = create_client(supabase_url = url, supabase_key = key)

def signIn(request):
    return render(request,"Login.html")

def postsignIn(request):
    email = request.POST.get('email')
    passw= request.POST.get('pass')
    try:
        user = supabase.auth.sign_up(email = email, password=passw)
        request.session["uid"] = str(user.id)
        return render(request,"jokes.html", {"email":email})
    except:
        print("paso aquí chu3rito")
        return render(request, "error.html")

def logout(request):
    try:
        del request.session['uid']
    except:
        pass
    return render(request,"Login.html")

def button(request):
    response = requests.get(url_api)
    jokes = response.json()["value"]
    print(jokes)
    return render(request, "jokes.html",{'jokes':jokes})

def buttonFav(request):
    value = request.GET.get("phrase")
    uid = request.session["uid"]
    supabase.table("phrases").insert({"phrase":value, 'user_id':uid}).execute()
    return render(request, "jokes.html")

def ButtonDelete(request, id):
    print(id)
    supabase.table("phrases").delete().eq("id",id).execute()

    return redirect('/list_Of_Jokes')

def list_Of_Jokes(request):
    list_jokes = supabase.table("phrases").select("*").eq("user_id", request.session["uid"]).execute()
    print(list_jokes.data)
    return render(request, "Listofjokes.html", {'phrase':list_jokes.data})
