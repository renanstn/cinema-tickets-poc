# Generated by Django 4.2.11 on 2024-07-23 00:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("cinema", "0002_remove_room_layout"),
    ]

    operations = [
        migrations.AlterField(
            model_name="chair",
            name="room",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="chairs",
                to="cinema.room",
            ),
        ),
    ]
