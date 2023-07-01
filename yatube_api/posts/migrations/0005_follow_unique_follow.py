# Generated by Django 3.2.16 on 2023-07-01 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_alter_follow_user'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.UniqueConstraint(fields=('user', 'following'), name='unique_follow'),
        ),
    ]
