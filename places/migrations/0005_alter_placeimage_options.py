# Generated by Django 3.2.6 on 2021-09-23 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_alter_placeimage_place'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='placeimage',
            options={'ordering': ['position']},
        ),
    ]