# Generated by Django 5.0.7 on 2024-10-08 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrower',
            name='borrower_id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
    ]
