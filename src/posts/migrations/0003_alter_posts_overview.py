# Generated by Django 5.1.3 on 2024-11-07 19:11

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_posts_featured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='overview',
            field=tinymce.models.HTMLField(),
        ),
    ]
