# Generated by Django 4.1.13 on 2024-01-04 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FlaggedAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.BigIntegerField(unique=True)),
                ('available_credit', models.BigIntegerField()),
                ('date_flagged', models.DateTimeField(auto_now_add=True)),
                ('amount', models.BigIntegerField()),
                ('KYC_incomplete', models.BooleanField()),
                ('multiple_accounts', models.BooleanField()),
                ('transaction_category', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FraudAlert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fraud_account', models.CharField(max_length=50)),
                ('confirming_station', models.CharField(max_length=50)),
                ('details', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]