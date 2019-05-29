from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('',views.home, name='homepage'),
    path('viz_1',views.Preprint_per_month, name='preprints per month'),
    # serializers
    path('_json/Tags', views.TagList.as_view()),
    path('_json/Preprints',views.PreprintList.as_view()),
    path('_json/Subjects', views.SubjectList.as_view()),
    path('_json/Authors', views.AuthorList.as_view()),

]

# urlpatterns = format_suffix_patterns(urlpatterns)