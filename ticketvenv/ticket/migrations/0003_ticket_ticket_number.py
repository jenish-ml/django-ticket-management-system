# Generated by Django 5.0.6 on 2024-06-25 09:06

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='ticket_number',
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]
