# Generated by Django 4.1.3 on 2022-12-12 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("zerver", "0424_rename_topic_name_streamtopic_name_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="realmauditlog",
            name="modified_stream_topic",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.CASCADE, to="zerver.streamtopic"
            ),
        ),
    ]
