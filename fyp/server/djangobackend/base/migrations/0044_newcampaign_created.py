# Generated by Django 3.2.18 on 2023-04-23 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0043_newcampaign_hashtag'),
    ]

    operations = [
        migrations.AddField(
            model_name='newcampaign',
            name='created',
            field = models.DateTimeField(auto_now_add = True)
        ),
    ]