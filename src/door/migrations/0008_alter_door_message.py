# Generated by Django 3.2.2 on 2021-05-13 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('door', '0007_door_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='door',
            name='message',
            field=models.CharField(blank=True, default=None, editable=False, max_length=255, null=True),
        ),
    ]
