# Generated by Django 4.1.7 on 2023-03-06 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_commentt'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-created_date']},
        ),
        migrations.AlterModelOptions(
            name='commentt',
            options={'ordering': ['-comment_date']},
        ),
    ]
