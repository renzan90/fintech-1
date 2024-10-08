# Generated by Django 5.0.7 on 2024-09-24 20:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Borrower',
            fields=[
                ('borrower_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('first_name', models.CharField(default='', max_length=15)),
                ('last_name', models.CharField(default='', max_length=15)),
                ('profession', models.CharField(default='', max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('ph_no', models.CharField(max_length=10, unique=True)),
                ('date_of_birth', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='BankDetails',
            fields=[
                ('borrower', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='user.borrower')),
                ('bank_name', models.CharField(max_length=25)),
                ('ifsc', models.CharField(max_length=25)),
                ('account_no', models.CharField(max_length=25)),
                ('upi_address', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='IncomeDocs',
            fields=[
                ('borrower', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='user.borrower')),
                ('form16', models.FileField(upload_to='')),
                ('bank_statement1', models.FileField(upload_to='')),
                ('bank_statement2', models.FileField(upload_to='')),
                ('profession', models.CharField(max_length=25)),
                ('salary_slip', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='KYC',
            fields=[
                ('borrower', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='user.borrower')),
                ('aadhar', models.CharField(max_length=25)),
                ('driving_license', models.FileField(upload_to='')),
                ('utility_bill', models.FileField(upload_to='')),
                ('pan', models.CharField(max_length=25)),
            ],
        ),
    ]
