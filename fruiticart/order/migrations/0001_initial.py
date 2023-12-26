# Generated by Django 4.2.1 on 2023-12-26 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('email', models.EmailField(max_length=50, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('phone_number', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=50)),
                ('postal_code', models.CharField(max_length=5)),
                ('credit_card', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('contact_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=50)),
                ('message', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_date', models.DateField()),
                ('delivery_date', models.DateField()),
                ('delivery_address', models.CharField(max_length=50)),
                ('delivery_postal_code', models.CharField(max_length=5)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Confirmed', 'Confirmed'), ('In transit', 'In transit'), ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled')], max_length=10)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.client')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('warehouse_id', models.AutoField(primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=50)),
                ('postal_code', models.CharField(max_length=5)),
                ('zone', models.CharField(choices=[('North', 'North'), ('South', 'South'), ('East', 'East'), ('West', 'West')], max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Vegetable',
            fields=[
                ('vegetable_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('origin', models.CharField(max_length=30)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.product')),
            ],
        ),
        migrations.CreateModel(
            name='Fruit',
            fields=[
                ('fruit_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('origin', models.CharField(max_length=30)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.product')),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('stock_id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.product')),
                ('warehouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.warehouse')),
            ],
            options={
                'unique_together': {('warehouse', 'product')},
            },
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('orderdetail_id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.product')),
            ],
            options={
                'unique_together': {('order', 'product')},
            },
        ),
    ]
