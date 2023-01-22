# Generated by Django 4.1.5 on 2023-01-19 00:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True, null=True, verbose_name='Created')),
                ('updated', models.DateField(auto_now=True, null=True, verbose_name='Updated')),
                ('image', models.ImageField(blank=True, null=True, upload_to='tiket/%(id)simages', verbose_name='Image')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='created_by%(app_label)s_%(class)s_related', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='updated_by%(app_label)s_%(class)s_related', to=settings.AUTH_USER_MODEL, verbose_name='Updated by')),
            ],
            options={
                'verbose_name': 'Files',
                'verbose_name_plural': 'Filess',
            },
        ),
        migrations.CreateModel(
            name='Tickets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True, null=True, verbose_name='Created')),
                ('updated', models.DateField(auto_now=True, null=True, verbose_name='Updated')),
                ('state', models.PositiveSmallIntegerField(choices=[(-1, 'Refused'), (0, 'Created'), (1, 'Assigned'), (2, 'In Process'), (3, 'Finalized')], default=0, verbose_name='State')),
                ('description', models.TextField(verbose_name='Description')),
                ('service', models.CharField(max_length=255, verbose_name='Service')),
                ('assigned_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assigned_to%(app_label)s_%(class)s_related', to=settings.AUTH_USER_MODEL, verbose_name='Assigned to')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='created_by%(app_label)s_%(class)s_related', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('images', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.files')),
                ('requesting_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requesting_by%(app_label)s_%(class)s_related', to=settings.AUTH_USER_MODEL, verbose_name='Requesting by')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='updated_by%(app_label)s_%(class)s_related', to=settings.AUTH_USER_MODEL, verbose_name='Updated by')),
            ],
            options={
                'verbose_name': 'Tickets',
                'verbose_name_plural': 'Ticketss',
            },
        ),
    ]