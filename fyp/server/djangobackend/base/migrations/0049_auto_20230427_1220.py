# Generated by Django 3.2.18 on 2023-04-27 07:20

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0048_auto_20230424_1130'),
    ]

    operations = [
        migrations.AddField(
            model_name='newcampaign',
            name='budget',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='newcampaign',
            name='campaign_type',
            field=models.CharField(choices=[('Periodic', 'Periodic'), ('Single', 'Single')], default='DEFAULT', max_length=20),
        ),
        migrations.AddField(
            model_name='newcampaign',
            name='hashtag',
            field=models.CharField(default='DEFAULT', max_length=50),
        ),
        migrations.AddField(
            model_name='newcampaign',
            name='influencers',
            field=models.ManyToManyField(blank=True, to='base.Influencer'),
        ),
        migrations.CreateModel(
            name='NewInfluencer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('influencerImage', models.ImageField(default='', upload_to='images/')),
                ('influencer_username', models.CharField(max_length=20)),
                ('influencer_full_name', models.CharField(max_length=200)),
                ('influencerInfluencerPostCost', models.IntegerField(blank=True, null=True)),
                ('influencerStoryCost', models.IntegerField(blank=True, null=True)),
                ('influencerChildrenCount', models.IntegerField(blank=True, null=True)),
                ('influencerChildrenAge', models.IntegerField(blank=True, null=True)),
                ('influencerInterests', models.CharField(choices=[('Fashion', 'Fashion'), ('Music', 'Music'), ('Food', 'Food'), ('Health', 'Health'), ('Gaming', 'Gaming'), ('Dance', 'Dance'), ('Entertainment', 'Entertainment'), ('Family', 'Family'), ('Kids', 'Kids')], max_length=20)),
                ('influencerGender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=20)),
                ('created', models.DateTimeField(default=datetime.datetime.now)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('engagement_rate', models.IntegerField(blank=True, default=0, null=True)),
                ('brandmanager', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.brandmanager')),
            ],
            options={
                'ordering': ['-updated', '-created'],
            },
        ),
    ]
