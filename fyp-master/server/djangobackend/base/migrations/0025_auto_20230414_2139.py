# Generated by Django 3.2.18 on 2023-04-14 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0024_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='influencer',
            name='image',
            field=models.ImageField(default='', upload_to='images/'),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
