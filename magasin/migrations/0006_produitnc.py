# Generated by Django 5.0.2 on 2024-02-26 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0005_fournisseur_adresse_fournisseur_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProduitNC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Duree_garantie', models.CharField(max_length=100)),
            ],
        ),
    ]
