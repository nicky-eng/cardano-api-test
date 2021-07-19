# Generated by Django 3.1 on 2021-07-19 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='googlemaps_link',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='store',
            name='picture',
            field=models.ImageField(blank=True, max_length=200, upload_to='media/'),
        ),
    ]