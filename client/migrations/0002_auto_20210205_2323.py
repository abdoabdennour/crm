# Generated by Django 3.0.5 on 2021-02-05 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='telephone',
            field=models.CharField(max_length=10),
        ),
    ]