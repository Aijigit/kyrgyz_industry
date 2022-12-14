# Generated by Django 4.0.8 on 2022-11-11 18:55

import django.core.validators
from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_alter_photosnews_url'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contests',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelOptions(
            name='gallerycontests',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelOptions(
            name='gallerynews',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelOptions(
            name='galleryproject',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelOptions(
            name='photoscontests',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelOptions(
            name='photosnews',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelOptions(
            name='photosproject',
            options={'ordering': ['-id']},
        ),
        migrations.RemoveField(
            model_name='contests',
            name='Category',
        ),
        migrations.RemoveField(
            model_name='contests',
            name='Description',
        ),
        migrations.RemoveField(
            model_name='contests',
            name='Gallery',
        ),
        migrations.RemoveField(
            model_name='contests',
            name='Short_Description',
        ),
        migrations.AlterField(
            model_name='contests',
            name='Document',
            field=models.FileField(upload_to=main.models.get_file_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx'])], verbose_name='Документ'),
        ),
        migrations.AlterField(
            model_name='contests',
            name='Status',
            field=models.CharField(choices=[('Актуально', 'Актуально'), ('Проведён', 'Проведён'), ('Не Проведён', 'Не Проведён')], default='Актуально', max_length=20, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='contests',
            name='Title',
            field=models.CharField(max_length=180, verbose_name='Описание конкурса'),
        ),
        migrations.AlterField(
            model_name='photosnews',
            name='URL',
            field=models.ImageField(upload_to=main.models.get_file_path, validators=[django.core.validators.validate_image_file_extension], verbose_name='Путь картинки'),
        ),
        migrations.AlterField(
            model_name='photosproject',
            name='URL',
            field=models.FileField(upload_to=main.models.get_file_path, verbose_name='Путь к картинке'),
        ),
    ]
