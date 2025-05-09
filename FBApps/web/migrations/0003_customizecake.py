# Generated by Django 5.1.1 on 2024-10-19 10:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0005_customers_otp'),
        ('web', '0002_alter_categories_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomizeCake',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('customize_cake_id', models.CharField(blank=True, max_length=255, primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='customize_cake/')),
                ('content', models.TextField()),
                ('request_status', models.CharField(blank=True, choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')], default='Pending', max_length=255, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.customers')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
