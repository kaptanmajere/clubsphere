# Generated by Django 4.0.5 on 2022-06-13 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0010_post_attendee_count_participationstate'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='picture',
            field=models.ImageField(blank=True, upload_to='club_pictures/'),
        ),
    ]
