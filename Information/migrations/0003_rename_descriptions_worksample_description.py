# Generated by Django 3.2.6 on 2021-09-05 22:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Information', '0002_auto_20210906_0310'),
    ]

    operations = [
        migrations.RenameField(
            model_name='worksample',
            old_name='Descriptions',
            new_name='Description',
        ),
    ]