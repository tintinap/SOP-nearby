# Generated by Django 2.2 on 2019-11-19 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nearby', '0002_place_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placeuser',
            name='ranking',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
