# Generated by Django 3.2 on 2021-05-20 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=models.FileField(blank=True, null=True, upload_to='profile_pics'),
        ),
    ]
