# Generated by Django 4.0.8 on 2022-11-08 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_photosproject_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photosnews',
            name='Gallery',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='main.gallerynews', verbose_name='Галерея'),
        ),
    ]
