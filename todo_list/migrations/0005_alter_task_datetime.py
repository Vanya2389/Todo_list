# Generated by Django 4.1 on 2023-03-15 16:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("todo_list", "0004_rename_tag_task_tags_alter_task_datetime_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="datetime",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]