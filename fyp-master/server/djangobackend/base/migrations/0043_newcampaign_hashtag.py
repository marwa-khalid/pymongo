# Generated by Django 3.2.18 on 2023-04-23 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0042_auto_20230423_2112'),
    ]

    operations = [
        migrations.AddField(
            model_name='newcampaign',
            name='hashtag',
            field=models.CharField(default='DEFAULT', max_length=50),
        ),
    ]
