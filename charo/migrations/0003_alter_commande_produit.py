# Generated by Django 4.2.7 on 2024-01-05 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('charo', '0002_article_prix'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commande',
            name='produit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='charo.article'),
        ),
    ]