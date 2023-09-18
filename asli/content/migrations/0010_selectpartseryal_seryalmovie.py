# Generated by Django 4.2.1 on 2023-09-14 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0009_category_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='SelectPartSeryal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('num_part', models.CharField(max_length=50)),
                ('part', models.FileField(upload_to='movies/')),
            ],
        ),
        migrations.CreateModel(
            name='SeryalMovie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('img', models.ImageField(upload_to='images/')),
                ('time', models.CharField(max_length=255)),
                ('worning', models.CharField(max_length=3)),
                ('date', models.CharField(max_length=20)),
                ('abut', models.TextField(blank=True, null=True)),
                ('category', models.ManyToManyField(related_name='part_movie', to='content.category')),
                ('part', models.ManyToManyField(related_name='part_seryal', to='content.selectpartseryal')),
            ],
        ),
    ]
