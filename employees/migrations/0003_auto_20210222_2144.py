# Generated by Django 3.1.7 on 2021-02-23 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_auto_20210222_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='admission_date',
            field=models.DateField(),
        ),
    ]