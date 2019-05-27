from django.shortcuts import render
import json
import urllib3 as url
from .models import Author,Subject,Preprint
from django.http import Http404
# Create your views here.

def home(request):

    # http = url.PoolManager()  #To handle all of the details of connection pooling and thread safety
    # r=http.request('GET','https://api.osf.io/v2/providers/preprints/africarxiv/preprints/?format=json')
    # dict = json.loads(r.data.decode('utf-8'))
    # #loading data from the json:api into a dictionary
    #
    # #TO_BE_CONTINUED

    return render(request,'homepage/home.html')

def general_stat(request):
    return render(request,'homepage/statistic.html')

def authors(request):
    all_authors=Author.objects.all()
    if not all_authors:
        home(request)    #to secure it and force the user to reload data from api

    context={'all_authors' : all_authors }
    return render(request,'homepage/Authors.html',context)

def preprints(request):
    all_preprints=Preprint.objects.all()
    if not all_preprints:
        home(request)    #to secure it and force the user to reload data from api

    return render(request,'homepage/Preprints.html',{'all_preprints' : all_preprints})


def auth_details(request,id):
    try:
        author = Author.objects.get(pk=id)
    except Author.DoesNotExist:
        raise Http404("Auteur inexistant")
    return render(request, 'homepage/auth_details.html', {'auteur': author})

def art_details(request,id):
    try:
        preprint = Preprint.objects.get(pk=id)
    except Preprint.DoesNotExist:
        raise Http404("article inexistant")
    return render(request, 'homepage/art_details.html', {'article': preprint})
