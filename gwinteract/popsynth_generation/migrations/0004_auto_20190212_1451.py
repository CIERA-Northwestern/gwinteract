# Generated by Django 2.1.4 on 2019-02-12 20:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('popsynth_generation', '0003_auto_20190212_1449'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newpopsynthmodel',
            old_name='B_0',
            new_name='b_0',
        ),
        migrations.RenameField(
            model_name='newpopsynthmodel',
            old_name='CK',
            new_name='ck',
        ),
    ]
