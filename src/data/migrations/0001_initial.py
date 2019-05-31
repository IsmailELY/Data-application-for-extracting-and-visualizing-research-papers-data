# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2019-05-31 06:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identity', models.CharField(max_length=100)),
                ('full_name', models.CharField(max_length=150)),
                ('region', models.CharField(max_length=20)),
                ('registration_date', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=200)),
                ('nombre_prep', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Preprint',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=250)),
                ('publication_date', models.DateField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('effectif_total', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('name', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('sujets', models.ManyToManyField(blank=True, to='data.Subject')),
            ],
        ),
        migrations.AddField(
            model_name='preprint',
            name='Subjects',
            field=models.ManyToManyField(blank=True, to='data.Subject'),
        ),
        migrations.AddField(
            model_name='preprint',
            name='tags',
            field=models.ManyToManyField(blank=True, to='data.Tag'),
        ),
        migrations.AddField(
            model_name='author',
            name='preprints',
            field=models.ManyToManyField(blank=True, to='data.Preprint'),
        ),
        migrations.AddField(
            model_name='author',
            name='relation_authors',
            field=models.ManyToManyField(blank=True, related_name='_author_relation_authors_+', to='data.Author'),
        ),
    ]