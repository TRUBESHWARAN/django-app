# Generated by Django 4.2.4 on 2023-09-16 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_alter_students_course_fee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='student_id',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
