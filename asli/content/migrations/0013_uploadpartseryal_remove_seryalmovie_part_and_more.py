# Generated by Django 4.2.1 on 2023-09-14 21:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0012_commentseryal_delete_commentcontenttype'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadPartSeryal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_part', models.CharField(max_length=50)),
                ('part', models.FileField(upload_to='movies/')),
            ],
        ),
        migrations.RemoveField(
            model_name='seryalmovie',
            name='part',
        ),
        migrations.DeleteModel(
            name='SelectPartSeryal',
        ),
        migrations.AddField(
            model_name='uploadpartseryal',
            name='seyal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='upload_part', to='content.seryalmovie'),
        ),
    ]
