# Generated by Django 5.0.2 on 2024-04-22 08:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0008_commande'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commande',
            name='produit',
        ),
        migrations.AddField(
            model_name='commande',
            name='produits',
            field=models.ManyToManyField(to='magasin.produit'),
        ),
        migrations.AlterField(
            model_name='commande',
            name='dateCde',
            field=models.DateField(default=datetime.date(2024, 4, 22), null=True),
        ),
        migrations.AlterField(
            model_name='commande',
            name='totalCde',
            field=models.FloatField(editable=False),
        ),
    ]
