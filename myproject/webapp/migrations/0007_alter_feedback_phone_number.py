# Generated by Django 5.0.1 on 2024-04-18 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_rename_name_feedback_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='Phone_Number',
            field=models.IntegerField(),
        ),
    ]
