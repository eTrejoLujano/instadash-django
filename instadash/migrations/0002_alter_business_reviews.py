# Generated by Django 4.2.1 on 2023-05-22 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instadash', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='reviews',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
