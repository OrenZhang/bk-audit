# Generated by Django 3.2.18 on 2023-10-19 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("risk", "0021_ticketpermission"),
    ]

    operations = [
        migrations.AddField(
            model_name="risk",
            name="last_operate_time",
            field=models.DateTimeField(auto_now=True, db_index=True, verbose_name="Last Operate Time"),
        ),
    ]
