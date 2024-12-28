# Generated by Django 5.0.10 on 2024-12-26 21:14

import django.db.models.deletion
import phonenumber_field.modelfields
from django.db import migrations, models

from ..choices import get_subject_default, get_subject_choices


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0035_auto_20230822_2208_squashed_0036_auto_20240311_1028'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='First name')),
                ('last_name', models.CharField(max_length=100, verbose_name='Last name')),
                ('profession', models.CharField(blank=True, default='', max_length=100, verbose_name='Profession')),
                ('subject', models.CharField(blank=True, choices=get_subject_choices(), default=get_subject_default(), max_length=55, verbose_name='Subject')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='Phone')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('message', models.TextField(verbose_name='Message')),
                ('data_confidentiality_policy', models.BooleanField(verbose_name='Data confidentiality policy')),
                ('ip_address', models.GenericIPAddressField()),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creation')),
            ],
            options={
                'verbose_name': 'request',
                'verbose_name_plural': 'requests',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='RequestPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='%(app_label)s_%(class)s', serialize=False, to='cms.cmsplugin')),
            ],
            bases=('cms.cmsplugin',),
        ),
    ]
