# Generated by Django 4.1.13 on 2024-01-09 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authDAS', '0002_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=200),
        ),
    ]
