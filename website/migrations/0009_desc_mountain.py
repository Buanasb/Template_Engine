# Generated by Django 3.2.4 on 2021-06-16 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_content_offer'),
    ]

    operations = [
        migrations.CreateModel(
            name='desc_mountain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('desc', models.CharField(max_length=100)),
            ],
        ),
    ]
