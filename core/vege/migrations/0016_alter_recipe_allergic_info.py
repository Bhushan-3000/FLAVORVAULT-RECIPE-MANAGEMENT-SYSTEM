# Generated by Django 5.0.6 on 2024-09-16 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0015_recipe_allergic_info_recipe_calories_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='allergic_info',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]