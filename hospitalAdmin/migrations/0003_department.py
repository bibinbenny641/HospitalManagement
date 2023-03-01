# Generated by Django 4.1.7 on 2023-02-27 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalAdmin', '0002_user_dob_user_user_name_alter_user_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DptName', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='pics/')),
                ('yearFounded', models.IntegerField()),
                ('description', models.CharField(max_length=255)),
            ],
        ),
    ]