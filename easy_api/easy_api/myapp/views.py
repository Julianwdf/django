from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.

def users(request):

    response = requests.get('https://jsonplaceholder.typicode.com/users')

    # convert response data into JSON
    users = response.json()
    print(users)

    return render(request, "users.html", {'users': users})
    pass
