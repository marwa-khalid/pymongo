# Generated by Django 3.2.18 on 2023-04-14 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0027_alter_influencer_engagement_rate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='influencer',
            name='engagement_rate',
        ),
    ]
