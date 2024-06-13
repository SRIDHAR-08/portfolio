# Generated by Django 5.0.6 on 2024-05-12 10:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_skill_skill_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume', models.FileField(default='null', upload_to='')),
                ('resume_photo1', models.ImageField(default='null', upload_to='')),
                ('resume_photo2', models.ImageField(default='null', upload_to='')),
                ('resume_photo3', models.ImageField(default='null', upload_to='')),
                ('resume_photo4', models.ImageField(default='null', upload_to='')),
                ('profile_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.profile_page')),
            ],
        ),
    ]
