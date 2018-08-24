# Generated by Django 2.0.1 on 2018-08-24 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0012_auto_20180822_1619'),
    ]

    operations = [
        migrations.CreateModel(
            name='AffiliationOption',
            fields=[
                ('name', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=75)),
            ],
        ),
        migrations.AddField(
            model_name='space',
            name='network_affiliation',
            field=models.ManyToManyField(blank=True, to='application.AffiliationOption'),
        ),
    ]