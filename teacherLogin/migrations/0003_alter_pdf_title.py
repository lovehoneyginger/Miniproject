# Generated by Django 4.0.5 on 2022-07-20 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacherLogin', '0002_pdf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pdf',
            name='title',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
    ]
