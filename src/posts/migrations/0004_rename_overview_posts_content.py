# Generated by Django 5.1.3 on 2024-11-08 09:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_alter_posts_overview'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posts',
            old_name='overview',
            new_name='content',
        ),
    ]
