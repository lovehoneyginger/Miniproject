# Generated by Django 3.2 on 2023-09-06 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacherLogin', '0004_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pdf',
            name='pdf',
            field=models.FileField(upload_to='pdf/'),
        ),
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.FileField(upload_to='videos/'),
        ),
    ]