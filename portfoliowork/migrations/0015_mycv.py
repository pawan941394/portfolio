# Generated by Django 4.0.6 on 2022-07-25 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfoliowork', '0014_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mycv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cvDate', models.CharField(max_length=255)),
                ('cv', models.FileField(upload_to='CV')),
            ],
        ),
    ]
