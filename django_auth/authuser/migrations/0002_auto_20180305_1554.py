# Generated by Django 2.0.2 on 2018-03-05 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authuser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='authuser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='authuser',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
    ]
