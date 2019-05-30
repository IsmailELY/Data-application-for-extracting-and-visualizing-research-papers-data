from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$',views.home, name='homepage'),
    url(r'^viz_1/$',views.Preprint_per_month, name='preprints per month'),
    url(r'^viz_2/$',views.Preprint_domination, name='preprints per field'),
    url(r'^viz_3/$',views.Tag_domination, name='Tags per domain'),
    url(r'^viz_4/$',views.Tag_domination, name='Tags per domain'),
    # serializers
    url(r'^json/Tags/$', views.TagList.as_view()),
    url(r'^json/Preprints/$',views.PreprintList.as_view()),
    url(r'^json/Subjects/$', views.SubjectList.as_view()),
    url(r'^json/Authors/$', views.AuthorList.as_view()),

]
