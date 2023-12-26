from django.db import models

class Fidelity(models.Model):
    type = models.CharField(max_length=7, primary_key=True)
    discount = models.DecimalField(max_digits=5, decimal_places=2)

class Client(models.Model):
    mail = models.EmailField(primary_key=True)
    password = models.CharField(max_length=50)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=10)
    address = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=5)
    credit_card = models.CharField(max_length=16)
    type = models.CharField(max_length=7, choices=[('Gold', 'Gold'), ('Silver', 'Silver'), ('Without', 'Without')])

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_date = models.DateField()
    delivery_date = models.DateField()
    delivery_address = models.CharField(max_length=50)
    delivery_postal_code = models.CharField(max_length=5)
    status = models.CharField(max_length=10, choices=[('Pending', 'Pending'), ('Confirmed', 'Confirmed'), ('In transit', 'In transit'), ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled')])
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    mail = models.ForeignKey(Client, on_delete=models.CASCADE)

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)

class Fruit(models.Model):
    fruit_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    origin = models.CharField(max_length=30)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class Vegetable(models.Model):
    vegetable_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    origin = models.CharField(max_length=30)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

class Warehouse(models.Model):
    warehouse_id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=5)
    zone = models.CharField(max_length=5, choices=[('North', 'North'), ('South', 'South'), ('East', 'East'), ('West', 'West')])

class Stock(models.Model):
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()