from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import SubjectSerializer,TagSerializer,AuthorSerializer,PreprintSerializer
import requests
from django.db import IntegrityError
import random

# Create your views here.


#home page and load data
def home(request):

    #Check if database is implemented for first time or not
    skip_heavy_load = False
    if Subject.objects.exists():
        skip_heavy_load=True


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
                for ide in lk:
                    aut.relation_authors.add(ide)
                lk.append(aut)
            preprint.save()

            #adding relation between tags and subjects
            for tg in preprint.tags.all():
                for sub in preprint.Subjects.all():
                    tg.sujets.add(sub)
                tg.save()

        #pagination
        if last_page == 1 or skip_heavy_load:
            break
        else:
            dict = requests.get(dict["links"]["next"]).json()
            if (dict["links"]["next"] == None):
                last_page = 1


    return  render(request,'home.html')


def Preprint_per_month(request):

    m = list()
    n = list()
    rdm = list()
    # # those lists will contain the date (yyyy-mm) and number_of_preprints and generate colors

    for pp in Preprint.objects.all():
        str1 = str(pp.publication_date.year)+'/'+str(pp.publication_date.month)
        if m==[] or str1 != m[0] :
            m.insert(0, str1)
            n.insert(0, 1)
            rdm.append(random.randint(1, 255))
        else:
             n[0] += 1
    data = {'mois' : m , "num" : n , "alea" : rdm}

    return render(request,'preprint_per_month.html',data)

def Preprint_domination(request):
    t_list=list()
    Osf_list=list()
    Afr_list=list()
    #initiate variables

    for sjt in Subject.objects.all():
        t_list.append(sjt.name)
        Osf_list.append(sjt.effectif_total)
        Afr_list.append(0)
    #getting the osf print number per field and fields name in a list

    for pp in Preprint.objects.all():
        for sbj in pp.Subjects.all():
            for i in range(len(t_list)):
                if sbj.name == t_list[i]:
                    Afr_list[i]+=1
    #filling the africarxiv number per subject

    data= { 'Sujets': t_list,'OSF':Osf_list,'AfricArXiv':Afr_list}

    return render(request,'preprint_per_subject.html',data)

def Tag_domination(request):
    t_list = list()
    tg_list = list()
    rdm = list()
    # initiate variables

    for sjt in Subject.objects.all():
        t_list.append(sjt.name)
        tg_list.append(0)
        rdm.append(random.randint(1, 255))
    # getting subject title and initializing our number of tags list

    for tg in Tag.objects.all():
        for sbj in tg.sujets.all():
            for i in range(len(t_list)):
                if sbj.name == t_list[i]:
                    tg_list[i]+=1

    data= { 'Sujets': t_list,'Tags': tg_list , 'alea': rdm}

    return render(request, 'tag_per_subject.html', data)

def Authors_division(request):

    Names = [ Author.objects.get(id=i+1).full_name for i in range(5) ]
    Prep_Num = [ Author.objects.get(id=i+1).nombre_prep for i in range(5) ]
    min = Prep_Num[0]
    idx_min = 0
    #initializing top authors list attributes

    Countries = list()
    Author_num = list()
    rdm = list()
    #initializing countries attributes

    for aut in Author.objects.all():

        #top 5 authors
        if min < aut.nombre_prep:
            Names[idx_min] = aut.full_name
            Prep_Num[idx_min] = aut.nombre_prep
            min = aut.nombre_prep

            for j in range(5):
                if min >= Prep_Num[j]:
                    min = Prep_Num[j]
                    idx_min = j

        #countries contribution
        if aut.region in Countries:
            index=Countries.index(aut.region)
            Author_num[index]+=1
        else:
            Countries.append(aut.region)
            Author_num.append(1)
            rdm.append(random.randint(1, 255))

    data = { 'Region': Countries,'NbrAut': Author_num , 'alea': rdm , 'liste_aut' : Names , 'nbr_art' : Prep_Num}

    return render(request,'author_per_country.html',data)

def Authors_network(request):
    l_aut = []
    l_link = []
    l_name = []
    l_num = []
    i=0
    #initialization

    for aut in Author.objects.all():

        l_aut.append(aut.id)
        l_name.append(aut.full_name)
        l_num.append(0)

        for lk in aut.relation_authors.all():
            l_link.append(lk.id)
            l_num[i]+=1
        i+=1

    data ={'authors':l_aut,'num':l_num,'relship':l_link,'names':l_name}

    return render(request,'authors_networks.html',data)



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
