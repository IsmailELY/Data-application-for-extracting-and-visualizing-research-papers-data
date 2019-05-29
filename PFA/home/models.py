from django.db import models

# Create your models here.





#Tag_model
class TagManager(models.Manager):
    def create_tag(self, Nom):
        tg = self.create(name=Nom)
        return tg

class Tag(models.Model):
    name = models.CharField(max_length=200,primary_key=True)

    objects = TagManager()

    def __str__(self):
        return self.name



#Subject_model
class SubjectManager(models.Manager):
    def create_subject(self, Id,name,efct):
        suj=self.create(id=Id,name=name,effectif_total=efct)
        return suj

class Subject(models.Model):
    id = models.CharField(max_length=200,primary_key=True)
    name = models.CharField(max_length=150)
    effectif_total=models.IntegerField()

    objects = SubjectManager()
    def __str__(self):
        return self.name



#Preprint_model
class PreprintManager(models.Manager):
    def create_preprint(self, Id, title, pub_d, descr):
        pp = self.create(id=Id,title=title,publication_date=pub_d,description=descr)
        return pp

class Preprint(models.Model):
    id = models.CharField(max_length=20,primary_key=True)
    title = models.CharField(max_length=250)
    publication_date = models.DateField()
    description = models.TextField()

    tags = models.ManyToManyField(Tag,blank=True)
    Subjects = models.ManyToManyField(Subject,blank=True)

    objects = PreprintManager()

    def __str__(self):
        return self.title




#Author_model

class AuthorManager(models.Manager):
    def create_author(self, Id, name, region, register_d ,image):
        aut = self.create(identity=Id,full_name=name,region=region,registration_date=register_d,image=image,nombre_prep=1)
        return aut

class Author(models.Model):
    identity = models.CharField(max_length=100)
    full_name = models.CharField(max_length=150)
    region = models.CharField(max_length=20)
    registration_date=models.CharField(max_length=100)
    image = models.CharField(max_length=200)
    nombre_prep=models.IntegerField()


    preprints = models.ManyToManyField(Preprint,blank=True)
    relation_authors=models.ManyToManyField("self",blank=True)

    objects = AuthorManager()

    def __str__(self):
        return self.full_name



