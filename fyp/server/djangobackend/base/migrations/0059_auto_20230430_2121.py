# Generated by Django 3.2.18 on 2023-04-30 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0058_rename_fullnname_newinfluencer_fullname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newinfluencer',
            old_name='ctorycost',
            new_name='storycost',
        ),
        migrations.AlterField(
            model_name='newinfluencer',
            name='isparent',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'no')], default='', max_length=20),
        ),
    ]
