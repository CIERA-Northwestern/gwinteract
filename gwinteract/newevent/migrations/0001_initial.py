# Generated by Django 2.1.4 on 2018-12-08 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GWEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('superevent_id', models.CharField(max_length=10)),
                ('gw_id', models.CharField(default=None, max_length=10)),
                ('preferred_event', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('posteriors_uploaded', models.BooleanField(default=False)),
                ('skymap_uploaded', models.BooleanField(default=False)),
                ('redshift_uploaded', models.BooleanField(default=False)),
            ],
        ),
    ]
