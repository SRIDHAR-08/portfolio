# Generated by Django 5.0.6 on 2024-05-13 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0016_alter_contect_message_send_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contect',
            name='message_send_at',
            field=models.CharField(default='null', max_length=30),
        ),
    ]
