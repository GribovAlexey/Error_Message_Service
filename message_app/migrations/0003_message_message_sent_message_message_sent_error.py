# Generated by Django 4.0.4 on 2022-06-10 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message_app', '0002_alter_message_user_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='message_sent',
            field=models.BooleanField(default=True, editable=False),
        ),
        migrations.AddField(
            model_name='message',
            name='message_sent_error',
            field=models.TextField(default='', editable=False),
        ),
    ]
