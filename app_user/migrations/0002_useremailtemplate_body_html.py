# Generated by Django 2.2.6 on 2019-10-29 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='useremailtemplate',
            name='body_html',
            field=models.TextField(default='', max_length=10000),
            preserve_default=False,
        ),
    ]
