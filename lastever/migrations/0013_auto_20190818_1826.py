# Generated by Django 2.2.4 on 2019-08-18 22:26

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('lastever', '0012_auto_20190818_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='text',
            field=tinymce.models.HTMLField(verbose_name='Content'),
        ),
    ]
