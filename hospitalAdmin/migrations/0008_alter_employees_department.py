# Generated by Django 4.1.7 on 2023-02-27 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalAdmin', '0007_remove_user_dob_remove_user_user_name_employees'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospitalAdmin.department'),
        ),
    ]
