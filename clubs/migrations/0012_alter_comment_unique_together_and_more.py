# Generated by Django 4.0.5 on 2022-06-13 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0011_club_picture'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='comment',
            unique_together={('post', 'user')},
        ),
        migrations.AlterUniqueTogether(
            name='participationstate',
            unique_together={('post', 'user')},
        ),
    ]
