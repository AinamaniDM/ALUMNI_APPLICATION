from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
        ('news', '0002_replace_uuid_with_integer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(max_length=5000, blank=True, null=True),
        ),
    ]