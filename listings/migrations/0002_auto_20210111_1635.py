# Generated by Django 3.1.4 on 2021-01-11 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
    ]