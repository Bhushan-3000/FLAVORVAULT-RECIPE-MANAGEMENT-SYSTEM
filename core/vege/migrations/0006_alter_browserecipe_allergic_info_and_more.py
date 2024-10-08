# Generated by Django 5.0.6 on 2024-09-04 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0005_remove_browserecipe_instructions_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='browserecipe',
            name='allergic_info',
            field=models.CharField(default='No info', max_length=1000),
        ),
        migrations.AlterField(
            model_name='browserecipe',
            name='description',
            field=models.CharField(max_length=800),
        ),
        migrations.AlterField(
            model_name='browserecipe',
            name='ingredients',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='browserecipe',
            name='instruction1',
            field=models.CharField(default='No info', max_length=1000),
        ),
        migrations.AlterField(
            model_name='browserecipe',
            name='instruction2',
            field=models.CharField(default='No info', max_length=1000),
        ),
        migrations.AlterField(
            model_name='browserecipe',
            name='instruction3',
            field=models.CharField(default='No info', max_length=1000),
        ),
        migrations.AlterField(
            model_name='browserecipe',
            name='recipe_name',
            field=models.CharField(max_length=500),
        ),
    ]
