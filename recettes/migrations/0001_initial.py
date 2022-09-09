# Generated by Django 4.1.1 on 2022-09-09 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("ingredients", "0002_alter_possessedingredient_expire_date_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Recipe",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("url", models.CharField(max_length=512)),
                ("name", models.CharField(max_length=256)),
                ("gluten_free", models.BooleanField(default=False)),
                ("lactose_free", models.BooleanField(default=False)),
                ("vegetarian", models.BooleanField(default=False)),
                ("vegan", models.BooleanField(default=False)),
                ("pork_free", models.BooleanField(default=False)),
                ("sweet", models.BooleanField(default=False)),
                ("salty", models.BooleanField(default=False)),
                ("ingredients", models.ManyToManyField(to="ingredients.ingredient")),
            ],
        ),
    ]
