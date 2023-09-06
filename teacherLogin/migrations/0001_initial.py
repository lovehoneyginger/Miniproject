# Generated by Django 4.0.5 on 2022-07-16 15:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=50)),
                ('branch', models.CharField(max_length=50)),
                ('teacher_id', models.CharField(max_length=11, unique=True)),
                ('gender', models.CharField(max_length=10)),
                ('dob', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('class_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('Year_of_introduction_of_class', models.IntegerField(null=True)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.subject')),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacherLogin.teacher', to_field='teacher_id')),
            ],
        ),
    ]
