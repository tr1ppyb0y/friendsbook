# Generated by Django 4.2.1 on 2023-05-13 08:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('profilepage', '0002_auto_20211013_0259'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profilepage',
            name='user_account',
        ),
        migrations.AddField(
            model_name='profilepage',
            name='content_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
        migrations.AddField(
            model_name='profilepage',
            name='object_id',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
