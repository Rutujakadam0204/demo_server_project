# Generated by Django 4.1.1 on 2022-09-15 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_core1_model3_uploaded_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='core1_model3',
            name='uploaded_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='document',
            name='uploaded_at',
            field=models.DateTimeField(),
        ),
    ]
