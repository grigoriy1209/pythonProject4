# Generated by Django 5.1.1 on 2024-09-25 16:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auto_parks', '0001_initial'),
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carmodel',
            name='auto_park',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='auto_parks.autoparkmodel'),
            preserve_default=False,
        ),
    ]