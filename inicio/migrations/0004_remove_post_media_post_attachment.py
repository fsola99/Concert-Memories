# Generated by Django 4.2.7 on 2023-11-12 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0003_alter_post_artista'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='media',
        ),
        migrations.AddField(
            model_name='post',
            name='attachment',
            field=models.ImageField(blank=True, null=True, upload_to='attachments'),
        ),
    ]