import re
import json
import pyrebase
import requests
from urllib import request, response
from django.shortcuts import redirect, render
from django.contrib import auth
from django.http import HttpResponse



config={
    'apiKey' : "AIzaSyD_6AVv3DvM6KfrKBnQJgqdyiR4otSDuQ0",
    'authDomain' : "logindjangoprueba.firebaseapp.com",
    'projectId' : "logindjangoprueba",
    'storageBucket' : "logindjangoprueba.appspot.com",
    'messagingSenderId' : "791591105335",
    'appId' : "1:791591105335:web:b71a9d2e8121b7717e20b2",
    'measurementId' : "G-HKL2L0NL1S",
    'databaseURL' : "https://logindjangoprueba-default-rtdb.firebaseio.com",
    "projectId": "logindjangoprueba"
}
firebase = pyrebase.initialize_app(config)
auth2 = firebase.auth()
database=firebase.database()
url = "https://api.chucknorris.io/jokes/random"

def signIn(request):
    return render(request,"Login.html")

def logout(request):
    try:
        del request.session['uid']
    except:
        pass
    return render(request,"Login.html")

def button(request):
    response = requests.get(url)
    jokes = response.json()["value"]
    print(jokes)
    return render(request, "jokes.html",{'jokes':jokes})

def buttonFav(request):
    query = request.GET.get("phrase")
    key = database.generate_key()
    database.child("phrase").child(key).set({'phrase':query, 'id':key})
    return render(request, "jokes.html")

def ButtonDelete(request, id):
    print(id)
    database.child('phrase').child(id).remove()

    return redirect('/list_Of_Jokes')


def postsignIn(request):
    email=request.POST.get('email')
    passw=request.POST.get('pass')
    try:

        user = auth2.sign_in_with_email_and_password(email,passw)
    except:
        print(user)
        message2="Invalid Credentials!!Please Check your Data"
        return render(request,"Login.html")
    session_id=user['idToken']
    request.session['uid']=str(session_id)
    return render(request,"jokes.html", {"email":email})

def list_Of_Jokes(request):
    try:
        request.session['uid']
    except:
        return render(request, "error.html")
    list_jokes = database.child('phrase').get().val()
    print('phrase')
    return render(request, "Listofjokes.html", {'phrase':list_jokes})
