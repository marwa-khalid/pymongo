# Generated by Django 3.2.18 on 2023-04-14 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0030_alter_influencer_engagement_ratee'),
    ]

    operations = [
        migrations.RenameField(
            model_name='influencer',
            old_name='engagement_ratee',
            new_name='engagement_rate',
        ),
    ]
