# Generated by Django 5.0.6 on 2024-05-12 10:17

import portfolio.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='resume',
            field=models.FileField(default='null', upload_to=portfolio.models.resume_img_FileName),
        ),
    ]