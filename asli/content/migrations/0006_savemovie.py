# Generated by Django 4.2.1 on 2023-09-13 00:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0005_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='SaveMovie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='save_movie', to='content.movie')),
            ],
        ),
    ]
