# Generated by Django 3.0.5 on 2020-05-25 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]