# Generated by Django 3.2.18 on 2023-04-23 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0041_alter_newcampaign_created'),
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
    ]
