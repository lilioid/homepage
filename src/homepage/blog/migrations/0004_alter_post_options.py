# Generated by Django 4.2.10 on 2024-02-22 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("homepage_blog", "0003_alter_category_options_alter_post_options_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="post",
            options={"ordering": ["-created_at"]},
        ),
    ]
