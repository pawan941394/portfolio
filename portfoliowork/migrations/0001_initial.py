# Generated by Django 4.0.6 on 2022-07-24 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='abousUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('para1', models.CharField(blank=True, max_length=3000)),
                ('para2', models.CharField(blank=True, max_length=2000)),
            ],
        ),
    ]