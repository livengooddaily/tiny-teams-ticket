# Generated by Django 3.2.4 on 2021-09-20 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_microsoftprofile_dark_mode_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='microsoftprofile',
            name='dark_mode_active',
            field=models.BooleanField(default=False, verbose_name='Dunkelmodus aktiviert?'),
        ),
        migrations.AlterField(
            model_name='microsoftprofile',
            name='receives_new_ticket_notifications',
            field=models.BooleanField(default=False, verbose_name='Neues Ticket Benachrichtigungen aktiviert?'),
        ),
        migrations.AlterField(
            model_name='microsoftprofile',
            name='teams_notifications_active',
            field=models.BooleanField(default=True, verbose_name='Benachrichtigungen aktiviert?'),
        ),
    ]
