# Generated by Django 5.0.6 on 2024-09-13 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0009_groceryitem_mealplan_cookingschedule'),
    ]

    operations = [
        migrations.RenameField(
            model_name='groceryitem',
            old_name='name',
            new_name='Item_name',
        ),
        migrations.RenameField(
            model_name='groceryitem',
            old_name='quantity',
            new_name='Quantity',
        ),
    ]
