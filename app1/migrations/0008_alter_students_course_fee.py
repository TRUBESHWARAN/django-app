# Generated by Django 4.2.4 on 2023-09-16 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_alter_students_student_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='course_fee',
            field=models.DecimalField(decimal_places=5, max_digits=7),
        ),
    ]
