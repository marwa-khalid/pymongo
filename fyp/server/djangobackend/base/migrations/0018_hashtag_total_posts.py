# Generated by Django 3.2.18 on 2023-04-09 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0017_campaigns'),
    ]

    operations = [
        migrations.AddField(
            model_name='hashtag',
            name='total_posts',
            field=models.IntegerField(default=0),
        ),
    ]
