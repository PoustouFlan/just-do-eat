# Generated by Django 4.1.1 on 2022-09-08 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("ingredients", "0001_initial"),
        ("recettes", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Recipy",
            new_name="Recipe",
        ),
    ]
