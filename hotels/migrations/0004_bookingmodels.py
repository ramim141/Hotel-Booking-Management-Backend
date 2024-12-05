# Generated by Django 5.0.4 on 2024-06-29 13:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0003_alter_hotel_district_alter_review_hotel_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BookingModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in', models.DateField()),
                ('check_out', models.DateField()),
                ('num_rooms', models.IntegerField(default=1)),
                ('total_cost', models.DecimalField(decimal_places=2, max_digits=12)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='hotels.hotel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
