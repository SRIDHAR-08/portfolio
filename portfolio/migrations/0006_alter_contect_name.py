# Generated by Django 5.0.6 on 2024-05-13 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_contect_alter_resume_resume_photo1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contect',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
