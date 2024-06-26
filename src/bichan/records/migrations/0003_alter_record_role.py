# Generated by Django 5.0.4 on 2024-06-10 01:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("records", "0002_record_role"),
    ]

    operations = [
        migrations.AlterField(
            model_name="record",
            name="role",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="records",
                to="auth.group",
            ),
        ),
    ]
