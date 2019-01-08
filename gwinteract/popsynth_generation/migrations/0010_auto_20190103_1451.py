# Generated by Django 2.1.4 on 2019-01-03 20:51

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('popsynth_generation', '0009_newpopsynthmodel_galaxy_component'),
    ]

    operations = [
        migrations.AddField(
            model_name='newpopsynthmodel',
            name='convergence_params',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=20), default=['mass_1', 'mass_2', 'porb', 'ecc'], size=None),
        ),
        migrations.AddField(
            model_name='newpopsynthmodel',
            name='final_kstar1',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), default=[13, 15], size=None),
        ),
        migrations.AddField(
            model_name='newpopsynthmodel',
            name='final_kstar2',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), default=[13, 15], size=None),
        ),
        migrations.AddField(
            model_name='newpopsynthmodel',
            name='initial_samp',
            field=models.CharField(choices=[('INDEPENDENT', 'independent'), ('MULTIDIM', 'multidim')], default='independent', max_length=20),
            preserve_default=False,
        ),
    ]