# Generated by Django 5.0.6 on 2024-09-04 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0004_browserecipe_delete_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='browserecipe',
            name='instructions',
        ),
        migrations.RemoveField(
            model_name='browserecipe',
            name='nutritional_info',
        ),
        migrations.AddField(
            model_name='browserecipe',
            name='allergic_info',
            field=models.CharField(default='No info', max_length=500),
        ),
        migrations.AddField(
            model_name='browserecipe',
            name='calories',
            field=models.CharField(default='No info', max_length=200),
        ),
        migrations.AddField(
            model_name='browserecipe',
            name='carbohydrates',
            field=models.CharField(default='No info', max_length=200),
        ),
        migrations.AddField(
            model_name='browserecipe',
            name='cooktime',
            field=models.CharField(default='No info', max_length=100),
        ),
        migrations.AddField(
            model_name='browserecipe',
            name='fats',
            field=models.CharField(default='No info', max_length=200),
        ),
        migrations.AddField(
            model_name='browserecipe',
            name='instruction1',
            field=models.CharField(default='No info', max_length=400),
        ),
        migrations.AddField(
            model_name='browserecipe',
            name='instruction2',
            field=models.CharField(default='No info', max_length=400),
        ),
        migrations.AddField(
            model_name='browserecipe',
            name='instruction3',
            field=models.CharField(default='No info', max_length=200),
        ),
        migrations.AddField(
            model_name='browserecipe',
            name='protein',
            field=models.CharField(default='No info', max_length=200),
        ),
        migrations.AddField(
            model_name='browserecipe',
            name='serve',
            field=models.CharField(default='No info', max_length=100),
        ),
        migrations.AddField(
            model_name='browserecipe',
            name='taste',
            field=models.CharField(default='No info', max_length=100),
        ),
    ]