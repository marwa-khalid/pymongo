# Generated by Django 3.2.18 on 2023-04-22 15:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0036_auto_20230419_2143'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewCampaign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(default=datetime.datetime.now)),
                ('created', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'ordering': ['-updated', '-created'],
            },
        ),
    ]
