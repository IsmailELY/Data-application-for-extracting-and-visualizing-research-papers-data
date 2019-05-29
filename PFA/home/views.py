from django.shortcuts import render,get_object_or_404,render_to_response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import SubjectSerializer,TagSerializer,AuthorSerializer,PreprintSerializer
import requests
from django.db import IntegrityError
import numpy as np
from bokeh.plotting import figure
from bokeh.io import show,output_file
from bokeh.embed import components
# Create your views here.


def home(request):
    #adding Subjects to database
    url = 'https://api.osf.io/v2/providers/preprints/africarxiv/taxonomies/highlighted/?format=json&fields[taxonomies]=text,child_count'
    json_data = requests.get(url).json()
    connexion_token_1=0
    try:
        for Sub in json_data['data']:
            try:
                sujet = Subject.objects.create_subject(Sub['id'], Sub['attributes']['text'],Sub['attributes']['child_count'])
                sujet.save()
            except IntegrityError:
                continue
    except KeyError:
        connexion_token_1+= 1
        print('La connexion au API AfricArXiv a echouee ! Tentative = ', connexion_token_1)
        if connexion_token_1==3:
            raise

    #filling_the_Preprints & Authors & Tags
    url='https://api.osf.io/v2/providers/preprints/africarxiv/preprints/?format=json'
    dict = requests.get(url).json()
    # storing the json in a dict
    last_page = 0

    while True:
        #test de connexion
        connexion_token_2=0
        try:
            nbr_1 = len(dict["data"])
        except KeyError:
            connexion_token_2+=1
            print('La connexion au API AfricArXiv a echouee ! Tentative = ',connexion_token_2)
            if connexion_token_2==3:
                raise
            continue


        for j in range(nbr_1):
            ddict=dict["data"][j]
            try:
                preprint = Preprint.objects.create_preprint(ddict['id'],ddict['attributes']['title'],ddict['attributes']['date_published'][:10],ddict['attributes']['description'])
            except IntegrityError:
                preprint = Preprint.objects.get(id=ddict['id'])

            #adding subjects to preprints
            for i in range(len(ddict['attributes']['subjects'])):
                for j in range(len(ddict['attributes']['subjects'][i])):
                    try:
                        sjt=Subject.objects.get(id=ddict['attributes']['subjects'][i][j]['id'])
                    except Subject.DoesNotExist:
                        continue
                    preprint.Subjects.add(sjt)

            #adding tags to preprints and tags to database
            for i in range(len(ddict['attributes']['tags'])):
                try:
                    tag = Tag.objects.get(name=ddict['attributes']['tags'][i])
                except Tag.DoesNotExist:
                    tag = Tag.objects.create_tag(ddict['attributes']['tags'][i])
                    tag.save()
                preprint.tags.add(tag)

            #adding authors to preprints and authors to database
            d = requests.get(ddict["relationships"]["contributors"]["links"]["related"]['href']).json()
            #list_of_linked_auth
            lk =list()
            for i in range(len(d["data"])):
                dd=d['data'][i]['embeds']['users']['data']
                try:
                    aut=Author.objects.get(identity=dd['id'])
                    aut.nombre_prep=+1
                    aut.preprints.add(preprint)
                except Author.DoesNotExist:
                    aut=Author.objects.create_author(dd['id'],dd['attributes']['full_name'],dd['attributes']['locale'],dd['attributes']['date_registered'],dd['links']['profile_image'])
                    aut.nombre_prep=1
                    aut.preprints.add(preprint)
                #create the link between authors
                for id in lk:
                    aut.relation_authors.add(id)
                lk.append(aut)
            preprint.save()

        #pagination
        if last_page == 1:
            break
        else:
            dict = requests.get(dict["links"]["next"]).json()
            if (dict["links"]["next"] == None):
                last_page = 1


    return  render(request,'home/home.html')


def Preprint_per_month(request):

    m = list()
    n = list()
    # # those lists will contain the date (yyyy-mm) and number_of_preprints
    #
    #
    for pp in Preprint.objects.all():
        str1 = str(pp.publication_date.year)+'/'+str(pp.publication_date.month)
        if m==[] or str1 != m[0] :
            m.insert(0, str1)
            n.insert(0, 1)
        else:
             n[0] += 1
    #
    # p = figure(x_range=m, plot_height=250, title= 'articles par mois',toolbar_location=None,tools="")
    #
    # p.vbar(x=m,top=n,width=0.9)
    #
    # p.xgrid.grid_line_color = None
    # p.y_range.start = 0
    #script , div = components(p)

    output_file('p_per_m.html')

    p = figure(plot_width=900, plot_height=600)
    p.vbar(x=[ i for i in range(len(m))], width=0.5, bottom=0,
           top=n, color="firebrick")

    show(p)
    return render_to_response('/home/preprint')


# serializers_object
class SubjectList(APIView):

    def get(self,request):
        subj = Subject.objects.all()
        serializer = SubjectSerializer(subj,many=True)
        return Response(serializer.data)

    def post(self):
        pass


class TagList(APIView):

    def get(self, request):
        tg = Tag.objects.all()
        serializer = TagSerializer(tg, many=True)
        return Response(serializer.data)

    def post(self):
        pass


class PreprintList(APIView):

    def get(self, request):
        pp = Preprint.objects.all()
        serializer = PreprintSerializer(pp, many=True)
        return Response(serializer.data)

    def post(self):
        pass


class AuthorList(APIView):

    def get(self, request):
        aut = Author.objects.all()
        serializer = AuthorSerializer(aut, many=True)
        return Response(serializer.data)

    def post(self):
        pass
