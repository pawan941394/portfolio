# Generated by Django 4.0.6 on 2022-07-24 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfoliowork', '0003_rename_para2_abousus_aboutus_1_remove_abousus_para1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='abousus',
            name='aboutus_2',
            field=models.TextField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='abousus',
            name='aboutus_1',
            field=models.TextField(blank=True, max_length=3000),
        ),
    ]
