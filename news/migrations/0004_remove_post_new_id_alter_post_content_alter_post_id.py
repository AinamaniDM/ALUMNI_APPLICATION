# Generated by Django 5.1.7 on 2025-03-22 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_remove_post_new_id_alter_post_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(blank=True, max_length=5000),
        ),
    ]
