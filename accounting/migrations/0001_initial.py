# Generated by Django 4.2.10 on 2024-02-27 05:38

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Bookings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('special_discount', models.PositiveIntegerField()),
                ('paid_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_method', models.CharField(choices=[('esewa', 'esewa'), ('khalti', 'khalti'), ('fhonepay', 'fhonepay')], default='esewa', max_length=50)),
                ('billing_date', models.DateField(auto_now_add=True)),
                ('is_paid', models.BooleanField(default=False)),
                ('payment_id', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('reservation', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Bookings.reservation')),
            ],
        ),
    ]