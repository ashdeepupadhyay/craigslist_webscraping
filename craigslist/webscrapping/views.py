from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
from requests.compat import quote_plus
from . import models 


# Create your views here.
BASE_CRAIGS_LIST_URL="https://delhi.craigslist.org/search/?query={}"
def home(request):
    return render(request,'base.html')

def new_search(request):
    search=request.POST.get('search')
    #print(quote_plus(search))
    models.Search.objects.create(search=search)
    final_url=BASE_CRAIGS_LIST_URL.format(quote_plus(search))
    print(final_url)
    #response=requests.get('https://delhi.craigslist.org/search/bbb?query=python&sort=rel')
    response = requests.get(final_url)
    data=response.text
    print(data)
    #print(search)
    stuff_for_frontend={
        'search':search
    }
    return render(request,'webscrapping/newsearch.html',stuff_for_frontend)