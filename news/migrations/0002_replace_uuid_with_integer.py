from django.db import migrations, models

def populate_new_ids(apps, schema_editor):
    Post = apps.get_model('news', 'Post')
    # Assign new integer IDs to existing records (starting from 1)
    for i, post in enumerate(Post.objects.all(), start=1):
        post.new_id = i
        post.save()

class Migration(migrations.Migration):
    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        # Step 1: Add a temporary integer column
        migrations.AddField(
            model_name='post',
            name='new_id',
            field=models.IntegerField(null=True),
        ),
        # Step 2: Populate new_id with sequential integers
        migrations.RunPython(
            code=populate_new_ids,
            reverse_code=lambda apps, schema_editor: None,  # No reverse for simplicity
        ),
        # Step 3: Drop the old UUID id column
        migrations.RunSQL(
            sql="ALTER TABLE news_post DROP COLUMN id;",
            reverse_sql="ALTER TABLE news_post ADD COLUMN id uuid DEFAULT uuid_generate_v1();"
        ),
        # Step 4: Rename new_id to id
        migrations.RunSQL(
            sql="ALTER TABLE news_post RENAME COLUMN new_id TO id;",
            reverse_sql="ALTER TABLE news_post RENAME COLUMN id TO new_id;"
        ),
        # Step 5: Set id as primary key with auto-increment
        migrations.RunSQL(
            sql=[
                "ALTER TABLE news_post ALTER COLUMN id SET NOT NULL;",
                "ALTER TABLE news_post ADD PRIMARY KEY (id);",
                "CREATE SEQUENCE news_post_id_seq OWNED BY news_post.id;",
                "SELECT setval('news_post_id_seq', (SELECT MAX(id) FROM news_post));",
                "ALTER TABLE news_post ALTER COLUMN id SET DEFAULT nextval('news_post_id_seq');",
            ],
            reverse_sql=[
                "ALTER TABLE news_post DROP CONSTRAINT news_post_pkey;",
                "DROP SEQUENCE news_post_id_seq;",
            ]
        ),
    ]