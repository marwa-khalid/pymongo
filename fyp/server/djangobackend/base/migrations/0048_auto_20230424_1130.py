# Generated by Django 3.2.18 on 2023-04-24 06:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0047_auto_20230424_0944'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newcampaign',
            options={},
        ),
        migrations.RemoveField(
            model_name='newcampaign',
            name='budget',
        ),
        migrations.RemoveField(
            model_name='newcampaign',
            name='campaign_type',
        ),
        migrations.RemoveField(
            model_name='newcampaign',
            name='created',
        ),
        migrations.RemoveField(
            model_name='newcampaign',
            name='hashtag',
        ),
        migrations.RemoveField(
            model_name='newcampaign',
            name='influencers',
        ),
        migrations.RemoveField(
            model_name='newcampaign',
            name='updated',
        ),
    ]
