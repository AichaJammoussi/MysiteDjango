# Generated by Django 5.0.2 on 2024-02-26 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0004_fournisseur_produit_fournisseur'),
    ]

    operations = [
        migrations.AddField(
            model_name='fournisseur',
            name='adresse',
            field=models.TextField(default='sfax'),
        ),
        migrations.AddField(
            model_name='fournisseur',
            name='email',
            field=models.EmailField(default='aa', max_length=254),
        ),
    ]
