# Generated by Django 3.0.6 on 2020-06-10 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0007_auto_20200610_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='tag',
            field=models.CharField(max_length=15, null=True, unique=True),
        ),
    ]