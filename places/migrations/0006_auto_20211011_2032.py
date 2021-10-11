# Generated by Django 3.2.6 on 2021-10-11 20:32

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0005_alter_placeimage_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place',
            old_name='description_short',
            new_name='short_description',
        ),
        migrations.RenameField(
            model_name='place',
            old_name='title_short',
            new_name='short_title',
        ),
        migrations.RenameField(
            model_name='place',
            old_name='description_long',
            new_name='long_description',
        ),
        migrations.AlterField(
            model_name='place',
            name='long_description',
            field=tinymce.models.HTMLField(blank=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='place',
            name='short_description',
            field=models.TextField(blank=True, verbose_name='Краткое описание'),
        ),
    ]
