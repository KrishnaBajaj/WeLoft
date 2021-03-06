# Generated by Django 2.0.13 on 2021-02-06 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('weloft', '0010_facilities'),
    ]

    operations = [
        migrations.CreateModel(
            name='Maintenance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AmtPayable', models.CharField(default='', max_length=100)),
                ('Apt_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weloft.Apartmentname')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
