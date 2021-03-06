# Generated by Django 3.0.6 on 2020-06-10 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0003_auto_20200609_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='snips', to='snippets.Tag'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='tag',
            field=models.CharField(blank=True, max_length=15, unique=True),
        ),
    ]
