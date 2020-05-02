# Generated by Django 3.0.5 on 2020-05-01 01:13

import account.models
from django.db import migrations, models
import phonenumber_field.modelfields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='OTP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otpref', models.CharField(blank=True, default=uuid.uuid4, max_length=100, unique=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('otpvalue', models.CharField(blank=True, default=account.models.otp_gen, max_length=20)),
                ('generation_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'OTP',
                'verbose_name_plural': 'OTPs',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(max_length=240)),
                ('last_name', models.CharField(max_length=240)),
                ('username', models.CharField(max_length=254, unique=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('dateOfBirth', models.DateTimeField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE'), ('OTHER', 'OTHER')], max_length=20, null=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to=account.models.avatar_upload_location)),
                ('bio', models.CharField(blank=True, max_length=512, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
        ),
    ]