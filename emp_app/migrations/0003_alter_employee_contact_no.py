# Generated by Django 5.0.2 on 2024-02-24 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp_app', '0002_department_role_employee_bonus_employee_contact_no_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='contact_No',
            field=models.IntegerField(default=0, max_length=100),
        ),
    ]
