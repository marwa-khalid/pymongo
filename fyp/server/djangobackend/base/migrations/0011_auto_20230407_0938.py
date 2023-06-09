# Generated by Django 3.2.18 on 2023-04-07 04:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_auto_20230407_0908'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campaign',
            name='host',
        ),
        migrations.RemoveField(
            model_name='influencer',
            name='campaigns',
        ),
        migrations.AddField(
            model_name='campaign',
            name='brand_manager',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.brandmanager'),
        ),
        migrations.AddField(
            model_name='campaign',
            name='influencers',
            field=models.ManyToManyField(blank=True, to='base.Influencer'),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='budget',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='campaign',
            name='campaign_type',
            field=models.CharField(choices=[('Periodic', 'Periodic'), ('Single', 'Single')], default='DEFAULT', max_length=20),
        ),
    ]
