# Generated by Django 3.1.7 on 2021-04-06 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('technoweb', '0006_auto_20210405_2238'),
    ]

    operations = [
        migrations.CreateModel(
            name='AskQuery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email', models.EmailField(max_length=254)),
            ],
        ),
    ]