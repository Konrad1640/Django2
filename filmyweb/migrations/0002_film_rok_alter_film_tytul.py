# Generated by Django 5.1.6 on 2025-02-17 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmyweb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='rok',
            field=models.PositiveSmallIntegerField(default=2000),
        ),
        migrations.AlterField(
            model_name='film',
            name='tytul',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]
