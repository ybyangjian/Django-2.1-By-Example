# Generated by Django 2.1.3 on 2018-12-02 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='auhtor',
            new_name='author',
        ),
    ]
