# Generated by Django 4.0.8 on 2022-11-11 18:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_alter_contests_options_alter_gallerycontests_options_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ContestsCategory',
        ),
        migrations.DeleteModel(
            name='GalleryContests',
        ),
        migrations.DeleteModel(
            name='PhotosContests',
        ),
    ]
