# Generated by Django 4.1.1 on 2023-08-01 23:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myschool', '0006_staff'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('class1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myschool.class')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myschool.staff')),
            ],
        ),
    ]
