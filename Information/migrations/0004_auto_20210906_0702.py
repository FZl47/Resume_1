# Generated by Django 3.2.6 on 2021-09-06 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Information', '0003_rename_descriptions_worksample_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('ValuePercent', models.CharField(max_length=5)),
            ],
        ),
        migrations.RemoveField(
            model_name='myinfo',
            name='Skills',
        ),
    ]
