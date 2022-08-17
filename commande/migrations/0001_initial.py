# Generated by Django 3.0.5 on 2021-02-06 00:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0002_auto_20210205_2323'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_crèation', models.DateTimeField(auto_now=True)),
                ('etat', models.CharField(choices=[('en instant', 'en instant'), ('livrè', 'livrè'), ('non livrè', 'non livrè')], max_length=50)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.Client')),
            ],
        ),
    ]