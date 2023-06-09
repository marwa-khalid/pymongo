# Generated by Django 3.2.18 on 2023-04-23 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0037_newcampaign'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newcampaign',
            options={},
        ),
        migrations.RemoveField(
            model_name='newcampaign',
            name='created',
        ),
        migrations.RemoveField(
            model_name='newcampaign',
            name='updated',
        ),
        migrations.AddField(
            model_name='newcampaign',
            name='campaign_name',
            field=models.CharField(default='DEFAULT', max_length=50),
        ),
        migrations.AddField(
            model_name='newcampaign',
            name='influencers',
            field=models.ManyToManyField(blank=True, to='base.Influencer'),
        ),
    ]
