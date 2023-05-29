from django.shortcuts import render
import requests

# Create your views here.
from django.shortcuts import render
from .forms import DictionaryForm

def oxford(request):
    search_result = {}
    if 'word' in request.GET:
        form = DictionaryForm(request.GET)
        if form.is_valid():
            search_result = form.search()
    else:
        form = DictionaryForm()
    return render(request, 'oxford.html', {'form': form, 'search_result': search_result})
