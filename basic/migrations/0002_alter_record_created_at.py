# Generated by Django 5.1.3 on 2024-11-07 12:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("basic", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="record",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]