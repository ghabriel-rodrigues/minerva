# Generated by Django 4.2.5 on 2023-11-04 04:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("relatos", "0002_alter_sentimentos_sentimento"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sentimentos",
            name="sentimento",
            field=models.CharField(
                choices=[
                    ("insatisfeito", "insatisfeito"),
                    ("irritado", "irritado"),
                    ("triste", "triste"),
                    ("chateado", "chateado"),
                    ("tranquilo", "tranquilo"),
                    ("alegre", "alegre"),
                    ("feliz", "feliz"),
                    ("satisfeito", "satisfeito"),
                ],
                default="tranquilo",
                max_length=12,
            ),
        ),
    ]
