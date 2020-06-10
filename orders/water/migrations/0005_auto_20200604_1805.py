# Generated by Django 3.0.5 on 2020-06-04 18:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("water", "0004_profile_role"),
    ]

    operations = [
        migrations.RemoveField(model_name="profile", name="user",),
        migrations.AlterField(
            model_name="order",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="orders",
                to="water.Profile",
            ),
        ),
    ]
