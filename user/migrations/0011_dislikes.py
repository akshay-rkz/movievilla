# Generated by Django 5.0.1 on 2024-05-07 09:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0005_notification'),
        ('user', '0010_remove_likes_userdislikes_remove_likes_userlikes'),
    ]

    operations = [
        migrations.CreateModel(
            name='DISlikes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movieid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.movies')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.customer')),
            ],
        ),
    ]