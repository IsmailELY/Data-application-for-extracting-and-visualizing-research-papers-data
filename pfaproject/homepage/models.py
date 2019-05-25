from django.db import models

# Create your models here.

class Subject(models.Model):
    Id = models.CharField(max_length=150,primary_key=True)
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Preprint(models.Model):
    title = models.CharField(max_length=250)
    publication_date = models.DateField()
    id = models.CharField(max_length=20,primary_key=True)
    description = models.TextField()

    Subjects = models.ForeignKey(Subject,null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Author(models.Model):
    Full_Name = models.CharField(max_length=150)
    id = models.CharField(max_length=20,primary_key=True)
    region = models.CharField(max_length=20)
    image = models.ImageField()
    registration_date=models.DateField()

    preprints = models.ManyToManyField(Preprint,blank=True)
    relation_authors=models.ManyToManyField("self",blank=True)

    def __str__(self):
        return self.Full_Name
