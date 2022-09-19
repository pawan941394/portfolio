# Generated by Django 4.0.6 on 2022-07-26 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfoliowork', '0016_alter_abousus_aboutus_1_alter_abousus_aboutus_2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Experience_name', models.CharField(blank=True, max_length=300)),
                ('Experience_image', models.ImageField(blank=True, upload_to='Certificate')),
                ('content', models.TextField(blank=True, max_length=2000)),
            ],
        ),
        migrations.AlterField(
            model_name='abousus',
            name='aboutus_1',
            field=models.TextField(blank=True, max_length=3000),
        ),
        migrations.AlterField(
            model_name='abousus',
            name='aboutus_2',
            field=models.TextField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='abousus',
            name='main_sub_heading',
            field=models.TextField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='content',
            field=models.TextField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='project',
            name='content',
            field=models.TextField(blank=True, max_length=2000),
        ),
    ]
