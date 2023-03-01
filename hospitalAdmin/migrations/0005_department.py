# Generated by Django 4.1.7 on 2023-02-27 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalAdmin', '0004_delete_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DptName', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='pics/')),
                ('yearFounded', models.IntegerField(null=True)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
    ]
