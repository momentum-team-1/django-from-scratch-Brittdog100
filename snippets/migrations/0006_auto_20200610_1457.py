# Generated by Django 3.0.6 on 2020-06-10 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0005_auto_20200610_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='tag',
            field=models.CharField(blank=True, max_length=15, null=True, unique=True),
        ),
    ]
